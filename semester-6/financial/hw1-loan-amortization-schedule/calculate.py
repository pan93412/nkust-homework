import polars as pl
from datetime import datetime, timedelta
from decimal import Decimal, ROUND_HALF_UP

from structure import LoanConfig, Method, PaymentFrequency


def calculate_payment_amount(principal: float, periods: int, annual_rate: float, method: Method) -> float:
    """計算每期應付金額（不含額外費用）"""
    if method == Method.EQUAL_PAYMENT:
        # 本息平均攤還法（俗稱房貸型）
        # 原理：每期支付相同的金額，但本金和利息的比例會隨著時間變化
        # 前期利息占比高，後期本金占比高
        monthly_rate = annual_rate / 12  # 月利率 = 年利率 / 12
        if monthly_rate == 0:
            # 如果利率為0，則每期只需歸還相同金額的本金
            return principal / periods
        # 貸款公式推導：
        # 1. 設每期還款金額為 PMT
        # 2. 設 r 為月利率、n 為期數、P 為本金
        # 3. 等比級數總和公式: P = PMT * (1 - (1+r)^-n) / r
        # 4. 解出 PMT: PMT = P * r * (1+r)^n / ((1+r)^n - 1)
        return principal * (monthly_rate * (1 + monthly_rate) ** periods) / ((1 + monthly_rate) ** periods - 1)
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
                if month == 12:
                    current_date = datetime(year + 1, 1, 1) - timedelta(days=1)
                else:
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
    
    # 計算基本還款金額（依據還款方式的不同而不同）
    base_payment = calculate_payment_amount(
        config.principal,
        total_periods,
        current_rate,
        config.method
    )
    
    # 生成還款日期列表
    payment_dates = get_payment_dates(
        config.start_date,
        total_periods,
        config.payment_frequency
    )
    
    # 準備攤銷表的資料結構
    data = {
        "期數": list(range(1, total_periods + 1)),
        "期初金額": [],  # 每期開始前的剩餘本金
        "每期支付額": [],  # 每期總支付額（本金+利息）
        "利息費用": [],  # 每期利息費用
        "本金償還": [],  # 每期償還本金
        "期末欠款": []   # 每期結束後的剩餘本金
    }
    
    # 計算每期攤還詳情
    for period in range(total_periods):
        # 檢查是否有利率變動（例如：浮動利率貸款）
        if config.interest_changes:
            for change in config.interest_changes:
                if payment_dates[period] >= change.effective_date:
                    current_rate = change.new_rate
        
        # 儲存期初金額（四捨五入到小數點後兩位）
        data["期初金額"].append(float(Decimal(str(remaining_principal)).quantize(Decimal("0.01"), ROUND_HALF_UP)))
        
        # 計算本期利息 = 剩餘本金 * 月利率（年利率/12）
        interest = remaining_principal * (current_rate / 12)
        
        # 處理寬限期（可能只需支付利息，暫不還本金）
        if config.grace_period and period < config.grace_period.months:
            # 寬限期內的還款計算
            if config.method == Method.EQUAL_PAYMENT:
                # 本息平均攤還法寬限期處理
                payment = base_payment  # 維持每期固定支付額
                interest_payment = interest  # 利息費用
                principal_payment = payment - interest  # 本金償還 = 支付額 - 利息
            else:  # EQUAL_PRINCIPAL（本金平均攤還法）
                payment = base_payment + interest  # 每期支付額 = 本金 + 利息
                principal_payment = base_payment  # 每期固定償還本金
                interest_payment = interest  # 利息費用
        else:
            # 正常還款期計算
            if config.method == Method.EQUAL_PAYMENT:
                # 本息平均攤還法
                payment = base_payment  # 基本還款金額
                interest_payment = interest  # 利息部分
                principal_payment = payment - interest  # 本金部分 = 總支付 - 利息
            else:  # EQUAL_PRINCIPAL（本金平均攤還法）
                principal_payment = base_payment  # 每期固定償還本金
                interest_payment = interest  # 利息部分
                payment = principal_payment + interest  # 每期支付額 = 本金 + 利息

        # 更新剩餘本金 = 目前剩餘本金 - 本期還款本金
        remaining_principal -= principal_payment
        
        # 儲存本期資料（四捨五入到小數點後兩位）
        data["每期支付額"].append(float(Decimal(str(payment)).quantize(Decimal("0.01"), ROUND_HALF_UP)))
        data["利息費用"].append(float(Decimal(str(interest_payment)).quantize(Decimal("0.01"), ROUND_HALF_UP)))
        data["本金償還"].append(float(Decimal(str(principal_payment)).quantize(Decimal("0.01"), ROUND_HALF_UP)))
        data["期末欠款"].append(float(Decimal(str(remaining_principal)).quantize(Decimal("0.01"), ROUND_HALF_UP)))
    
    # 轉換為 Polars DataFrame 並返回
    return pl.DataFrame(data)
