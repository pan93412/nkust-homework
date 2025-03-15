import polars as pl
from datetime import datetime, timedelta
from decimal import Decimal, ROUND_HALF_UP

from structure import LoanConfig, Method, PaymentFrequency, PaymentType, InterestPeriod


def calculate_payment_amount(principal: float, periods: int, annual_rate: float, method: Method, payment_frequency: PaymentFrequency = PaymentFrequency.MONTHLY) -> float:
    """計算每期應付金額（不含額外費用）"""
    # 根據還款頻率調整利率
    if payment_frequency == PaymentFrequency.MONTHLY:
        period_rate = annual_rate / 12  # 月利率 = 年利率 / 12個月
    elif payment_frequency == PaymentFrequency.BIWEEKLY:
        period_rate = annual_rate / 26  # 雙週利率 = 年利率 / 26個雙週
    else:  # WEEKLY
        period_rate = annual_rate / 52  # 週利率 = 年利率 / 52個週
        
    if method == Method.EQUAL_PAYMENT:
        # 本息平均攤還法（俗稱房貸型）
        # 原理：每期支付相同的金額，但本金和利息的比例會隨著時間變化
        # 前期利息占比高，後期本金占比高
        if period_rate == 0:
            # 如果利率為0，則每期只需歸還相同金額的本金
            return principal / periods
        # 貸款公式推導：
        # 1. 設每期還款金額為 PMT
        # 2. 設 r 為期利率、n 為期數、P 為本金
        # 3. 等比級數總和公式: P = PMT * (1 - (1+r)^-n) / r
        # 4. 解出 PMT: PMT = P * r * (1+r)^n / ((1+r)^n - 1)
        return principal * (period_rate * (1 + period_rate) ** periods) / ((1 + period_rate) ** periods - 1)
    else:
        # 本金平均攤還法（俗稱企業貸款型）
        # 原理：每期償還相同金額的本金，但利息會隨著剩餘本金減少而遞減
        # 因此，每期總還款金額會隨時間遞減
        return principal / periods  # 每期應還本金 = 總本金 / 總期數


def get_payment_dates(start_date: datetime, periods: int, frequency: PaymentFrequency) -> list[datetime]:
    """根據還款頻率計算每期還款日期"""
    dates = []
    current_date = start_date
    
    if frequency == PaymentFrequency.MONTHLY:
        # 月付款頻率：每期相隔一個月
        for _ in range(periods):
            dates.append(current_date)
            # 加一個月，需特別處理月底日期
            year = current_date.year + (current_date.month == 12)
            month = (current_date.month % 12) + 1
            
            # 處理月底日期，例如 1/31 -> 2/28
            try:
                current_date = current_date.replace(year=year, month=month)
            except ValueError:
                # 如果日期超出範圍，則使用該月最後一天
                # 注意：當 month == 12 時，不會進入這個例外處理，因為 12 月有 31 天
                # 所以這裡不需要特別處理 month == 12 的情況
                current_date = datetime(year, month + 1, 1) - timedelta(days=1)
    else:
        # 雙週或每週還款：分別相隔14天或7天
        days = 14 if frequency == PaymentFrequency.BIWEEKLY else 7
        for _ in range(periods):
            dates.append(current_date)
            current_date += timedelta(days=days)
    
    return dates


def calculate_loan_amortization(config: LoanConfig) -> pl.DataFrame:
    '''
    計算貸款攤銷表

    Args:
        config (LoanConfig): 貸款設定

    Returns:
        pl.DataFrame: 貸款攤銷表
    '''
    # 初始化基本變數
    remaining_principal = float(config.principal)  # 剩餘本金，初始值為貸款總額
    current_rate = config.annual_rate  # 目前年利率
    total_periods = config.periods  # 總期數
    
    # 計算基本還款金額（依據還款方式和還款頻率的不同而不同）
    base_payment = calculate_payment_amount(
        config.principal,
        total_periods,
        current_rate,
        config.method,
        config.payment_frequency
    )
    
    # 生成還款日期列表
    payment_dates = get_payment_dates(
        config.start_date,
        total_periods,
        config.payment_frequency
    )

    # 如果是月底付款，且是每月還款頻率，將日期調整到月底
    if config.payment_type == PaymentType.END and config.payment_frequency == PaymentFrequency.MONTHLY:
        payment_dates = [
            (datetime(date.year, date.month + 1, 1) - timedelta(days=1))
            if date.month != 12
            else datetime(date.year + 1, 1, 1) - timedelta(days=1)
            for date in payment_dates
        ]
    
    # 準備攤銷表的資料結構
    data = {
        "期數": list(range(1, total_periods + 1)),
        "還款日期": payment_dates,
        "期初金額": [],
        "每期支付額": [],
        "利息費用": [],
        "本金償還": [],
        "服務費": [],
        "帳戶管理費": [],
        "保證手續費": [],
        "總費用": [],
        "期末欠款": []
    }
    
    # 計算開辦費（一次性收取）
    setup_fee = config.fees.setup_fee if config.fees else 0
    
    # 計算每期攤還詳情
    for period in range(total_periods):
        # 檢查是否有利率變動
        if config.interest_changes:
            for change in config.interest_changes:
                if payment_dates[period] >= change.effective_date:
                    current_rate = change.new_rate
        
        # 儲存期初金額
        data["期初金額"].append(float(Decimal(str(remaining_principal)).quantize(Decimal("0.01"), ROUND_HALF_UP)))
        
        # 根據計息週期計算利息
        # 注意：這裡假設不同計息週期的利率已經在 annual_rate 中考慮
        interest_multiplier = 1  # 預設為月計息
        if config.interest_period == InterestPeriod.QUARTERLY:
            interest_multiplier = 3
        elif config.interest_period == InterestPeriod.HALF_YEARLY:
            interest_multiplier = 6
        elif config.interest_period == InterestPeriod.YEARLY:
            interest_multiplier = 12
            
        # 計算本期利息（根據還款頻率調整）
        # 計算期利率，與 calculate_payment_amount 保持一致
        if config.payment_frequency == PaymentFrequency.MONTHLY:
            period_rate = current_rate / 12
        elif config.payment_frequency == PaymentFrequency.BIWEEKLY:
            period_rate = current_rate / 26
        else:  # WEEKLY
            period_rate = current_rate / 52
            
        # 考慮計息週期
        interest = remaining_principal * period_rate * interest_multiplier
            
        # 如果不是每月計息，則需要判斷是否為計息日
        if interest_multiplier > 1:
            # 判斷目前期數是否為計息期
            is_interest_period = (period % interest_multiplier) == 0
            if not is_interest_period:
                interest = 0  # 非計息期不計算利息
        
        # 計算各項費用
        if config.fees:
            # 服務費 = 剩餘本金 × 服務費率 / 12（假設服務費率為年率）
            service_fee = remaining_principal * (config.fees.service_fee_rate / 12)
            # 帳戶管理費（固定金額）
            account_fee = config.fees.account_management_fee
            # 保證手續費 = 剩餘本金 × 保證手續費率 / 12
            guarantee_fee = remaining_principal * (config.fees.guarantee_fee_rate / 12)
        else:
            service_fee = account_fee = guarantee_fee = 0
            
        # 處理寬限期
        if config.grace_period and period < config.grace_period.months:
            if config.method == Method.EQUAL_PAYMENT:
                payment = base_payment
                interest_payment = interest
                principal_payment = payment - interest
            else:
                payment = base_payment + interest
                principal_payment = base_payment
                interest_payment = interest
        else:
            if config.method == Method.EQUAL_PAYMENT:
                payment = base_payment
                interest_payment = interest
                principal_payment = payment - interest
            else:
                principal_payment = base_payment
                interest_payment = interest
                payment = principal_payment + interest

        # 更新剩餘本金
        remaining_principal -= principal_payment
        
        # 計算總費用
        total_fees = service_fee + account_fee + guarantee_fee
        if period == 0:  # 第一期加上開辦費
            total_fees += setup_fee
        
        # 儲存本期資料（四捨五入到小數點後兩位）
        data["每期支付額"].append(float(Decimal(str(payment + total_fees)).quantize(Decimal("0.01"), ROUND_HALF_UP)))
        data["利息費用"].append(float(Decimal(str(interest_payment)).quantize(Decimal("0.01"), ROUND_HALF_UP)))
        data["本金償還"].append(float(Decimal(str(principal_payment)).quantize(Decimal("0.01"), ROUND_HALF_UP)))
        data["服務費"].append(float(Decimal(str(service_fee)).quantize(Decimal("0.01"), ROUND_HALF_UP)))
        data["帳戶管理費"].append(float(Decimal(str(account_fee)).quantize(Decimal("0.01"), ROUND_HALF_UP)))
        data["保證手續費"].append(float(Decimal(str(guarantee_fee)).quantize(Decimal("0.01"), ROUND_HALF_UP)))
        data["總費用"].append(float(Decimal(str(total_fees)).quantize(Decimal("0.01"), ROUND_HALF_UP)))
        data["期末欠款"].append(float(Decimal(str(remaining_principal)).quantize(Decimal("0.01"), ROUND_HALF_UP)))
    
    # 轉換為 Polars DataFrame 並返回
    return pl.DataFrame(data)
