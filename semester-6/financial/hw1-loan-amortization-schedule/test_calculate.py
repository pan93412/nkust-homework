from datetime import datetime

from calculate import calculate_payment_amount, get_payment_dates, calculate_loan_amortization
from structure import LoanConfig, Method, PaymentFrequency, GracePeriod, InterestChange, PaymentType, InterestPeriod, Fees, PrepaymentOptions


class TestCalculatePaymentAmount:
    """測試每期應付金額計算函數"""

    def test_equal_payment_method(self):
        """測試本息平均攤還法（等額本息）
        
        這種還款方式下，每期償還金額相同，但前期利息佔比高，後期本金佔比高。
        此測試驗證公式：PMT = P * r * (1+r)^n / ((1+r)^n - 1)

        PMT (Payment) 指每期的還款金額
        P (Principal) 指貸款本金總額
        r (rate) 指每期的利率（若年利率為5%，而每月還款，則r = 0.05/12 = 0.00417）
        n 指總還款期數（若貸款30年，每月還款，則n = 30*12 = 360）
        """
        # 測試案例：借款 1,000,000，年利率 3.6%，期數 12 個月
        principal = 1000000
        periods = 12
        annual_rate = 0.036
        
        # 手動計算預期結果
        monthly_rate = annual_rate / 12
        expected_payment = principal * (monthly_rate * (1 + monthly_rate) ** periods) / ((1 + monthly_rate) ** periods - 1)
        
        # 使用函數計算結果
        result = calculate_payment_amount(principal, periods, annual_rate, Method.EQUAL_PAYMENT)
        
        # 驗證結果（允許小數點後兩位的誤差）
        assert round(result, 2) == round(expected_payment, 2)

    def test_equal_principal_method(self):
        """測試本金平均攤還法（等額本金）
        
        這種還款方式下，每期本金還款金額相同，但利息隨著本金減少而遞減，
        因此總還款金額會逐漸減少。此測試驗證公式：每期本金 = 本金 / 期數
        """
        principal = 1000000
        periods = 12
        annual_rate = 0.036
        
        # 使用函數計算結果
        result = calculate_payment_amount(principal, periods, annual_rate, Method.EQUAL_PRINCIPAL)
        
        # 驗證結果（本金平均攤還法中，每期本金固定為總本金除以期數）
        assert result == principal / periods
        assert result == 83333.33333333333  # 每期還款本金

    def test_zero_interest_rate(self):
        """測試零利率情況
        
        當利率為 0 時，兩種還款方法應該產生相同的每期還款金額：本金 / 期數
        """
        principal = 1000000
        periods = 12
        annual_rate = 0.0
        
        # 測試等額本息
        result_equal_payment = calculate_payment_amount(principal, periods, annual_rate, Method.EQUAL_PAYMENT)
        # 測試等額本金
        result_equal_principal = calculate_payment_amount(principal, periods, annual_rate, Method.EQUAL_PRINCIPAL)
        
        # 驗證兩種方法在零利率時結果相同
        assert result_equal_payment == result_equal_principal
        assert result_equal_payment == principal / periods


class TestGetPaymentDates:
    """測試還款日期計算函數"""

    def test_monthly_payment_dates(self):
        """測試每月還款日期計算
        
        驗證每月還款日期是否正確增加一個月，包括跨年和月底處理。
        """
        start_date = datetime(2023, 1, 15)
        periods = 3
        
        # 使用函數計算結果
        result = get_payment_dates(start_date, periods, PaymentFrequency.MONTHLY)
        
        # 驗證結果
        expected = [
            datetime(2023, 1, 15),
            datetime(2023, 2, 15),
            datetime(2023, 3, 15)
        ]
        assert result == expected

    def test_biweekly_payment_dates(self):
        """測試雙週還款日期計算
        
        驗證每兩週還款日期是否正確增加 14 天。
        """
        start_date = datetime(2023, 1, 15)
        periods = 3
        
        # 使用函數計算結果
        result = get_payment_dates(start_date, periods, PaymentFrequency.BIWEEKLY)
        
        # 驗證結果
        expected = [
            datetime(2023, 1, 15),
            datetime(2023, 1, 29),
            datetime(2023, 2, 12)
        ]
        assert result == expected

    def test_weekly_payment_dates(self):
        """測試每週還款日期計算
        
        驗證每週還款日期是否正確增加 7 天。
        """
        start_date = datetime(2023, 1, 15)
        periods = 3
        
        # 使用函數計算結果
        result = get_payment_dates(start_date, periods, PaymentFrequency.WEEKLY)
        
        # 驗證結果
        expected = [
            datetime(2023, 1, 15),
            datetime(2023, 1, 22),
            datetime(2023, 1, 29)
        ]
        assert result == expected

    def test_month_end_handling(self):
        """測試月底處理
        
        測試月底日期處理是否正確，特別是從 12 月到 1 月的轉換。
        """
        start_date = datetime(2023, 12, 31)
        periods = 2
        
        # 使用函數計算結果
        result = get_payment_dates(start_date, periods, PaymentFrequency.MONTHLY)
        
        # 驗證結果（注意跨年處理）
        expected = [
            datetime(2023, 12, 31),
            datetime(2024, 1, 31)
        ]
        assert result == expected

    def test_december_month_end_handling(self):
        """測試 12 月月底轉 1 月處理
        
        特別測試從 12 月月底到下一年 1 月的日期處理。
        """
        # 測試需要執行日期超出範圍的邏輯，所以用 12 月 31 日作為開始日期
        # 然後嘗試加一個月，會超出範圍，進入 if month == 12 的分支
        start_date = datetime(2023, 12, 30)
        periods = 3
        
        # 使用函數計算結果
        result = get_payment_dates(start_date, periods, PaymentFrequency.MONTHLY)
        
        # 驗證結果（注意測試以下日期計算）
        # 1. 從 12 月 30 日到 1 月 30 日（正常計算）
        # 2. 從 1 月 30 日到 2 月（會超出範圍，因為 2 月沒有 30 日）
        # 3. 從 2 月最後一天到 3 月（再次測試月底處理）
        expected = [
            datetime(2023, 12, 30),
            datetime(2024, 1, 30),
            datetime(2024, 2, 29)  # 2024 年是閏年，所以 2 月有 29 天
        ]
        assert result == expected

    def test_month_31_to_month_31_handling(self):
        """測試月底日期處理，特別是從 12 月 31 日到 1 月 31 日的處理
        
        此測試目的是觸發 get_payment_dates 函數中 if month == 12 的分支
        """
        # 我們需要 12 月 31 日作為日期，並且下一個月是 1 月，這會觸發 month == 12 的分支
        start_date = datetime(2022, 12, 31)
        periods = 2
        
        # 使用函數計算結果
        result = get_payment_dates(start_date, periods, PaymentFrequency.MONTHLY)
        
        # 第一個日期應該是起始日期
        assert result[0] == datetime(2022, 12, 31)
        
        # 第二個日期應該是 1 月 31 日
        # 這應該會觸發 if month == 12 的分支，因為 12 月變成 1 月會進入 ValueError 例外處理
        assert result[1] == datetime(2023, 1, 31)


class TestCalculateLoanAmortization:
    """測試貸款攤銷表計算函數"""

    def test_equal_payment_amortization(self):
        """測試本息平均攤還法攤銷表計算
        
        測試等額本息方式下的攤銷表計算，驗證以下重點：
        1. 每期還款金額應相同
        2. 總還款額應等於本金和利息的總和
        3. 最後一期後，剩餘本金應接近於零
        """
        # 設定貸款參數
        config = LoanConfig(
            principal=1000000,
            periods=12,
            annual_rate=0.036,
            start_date=datetime(2023, 1, 1),
            method=Method.EQUAL_PAYMENT
        )
        
        # 使用函數計算攤銷表
        result_df = calculate_loan_amortization(config)
        
        # 提取結果數據
        payments = result_df["每期支付額"].to_list()
        interest_expenses = result_df["利息費用"].to_list()
        principal_repayments = result_df["本金償還"].to_list()
        final_balance = result_df["期末欠款"].to_list()[-1]
        
        # 驗證每期還款金額相同（允許小數點後兩位的誤差）
        first_payment = payments[0]
        assert all(abs(payment - first_payment) < 0.03 for payment in payments)
        
        # 驗證利息和本金之和等於每期支付額
        for i in range(len(payments)):
            assert abs(interest_expenses[i] + principal_repayments[i] - payments[i]) < 0.03
        
        # 驗證最後一期後，剩餘本金接近於零
        assert abs(final_balance) < 0.1
        
        # 驗證本金償還總和接近貸款本金
        total_principal_repaid = sum(principal_repayments)
        assert abs(total_principal_repaid - config.principal) < 0.1

    def test_equal_principal_amortization(self):
        """測試本金平均攤還法攤銷表計算
        
        測試等額本金方式下的攤銷表計算，驗證以下重點：
        1. 每期償還本金應相同
        2. 利息費用應隨著本金減少而遞減
        3. 總還款額應等於本金和利息的總和
        4. 最後一期後，剩餘本金應接近於零
        """
        # 設定貸款參數
        config = LoanConfig(
            principal=1000000,
            periods=12,
            annual_rate=0.036,
            start_date=datetime(2023, 1, 1),
            method=Method.EQUAL_PRINCIPAL
        )
        
        # 使用函數計算攤銷表
        result_df = calculate_loan_amortization(config)
        
        # 提取結果數據
        payments = result_df["每期支付額"].to_list()
        interest_expenses = result_df["利息費用"].to_list()
        principal_repayments = result_df["本金償還"].to_list()
        final_balance = result_df["期末欠款"].to_list()[-1]
        
        # 驗證每期本金償還相同（允許小數點後兩位的誤差）
        first_principal = principal_repayments[0]
        assert all(abs(p - first_principal) < 0.03 for p in principal_repayments)
        
        # 驗證利息遞減（第一期利息應大於最後一期利息）
        assert interest_expenses[0] > interest_expenses[-1]
        
        # 驗證利息和本金之和等於每期支付額
        for i in range(len(payments)):
            assert abs(interest_expenses[i] + principal_repayments[i] - payments[i]) < 0.03
        
        # 驗證最後一期後，剩餘本金接近於零
        assert abs(final_balance) < 0.1
        
        # 驗證本金償還總和接近貸款本金
        total_principal_repaid = sum(principal_repayments)
        assert abs(total_principal_repaid - config.principal) < 0.1

    def test_with_grace_period(self):
        """測試含寬限期的攤銷表計算
        
        測試有寬限期的情況下的攤銷表計算，驗證以下重點：
        1. 寬限期內的還款處理是否正確
        2. 寬限期後的還款計算是否正確
        """
        # 建立寬限期物件
        grace_period = GracePeriod()
        grace_period.months = 3
        
        # 設定貸款參數
        config = LoanConfig(
            principal=1000000,
            periods=12,
            annual_rate=0.036,
            start_date=datetime(2023, 1, 1),
            method=Method.EQUAL_PAYMENT,
            grace_period=grace_period
        )
        
        # 使用函數計算攤銷表
        result_df = calculate_loan_amortization(config)
        
        # 提取結果數據
        remaining_balances = result_df["期末欠款"].to_list()
        
        # 驗證寬限期內本金是否減少較少（因為部分還款可能主要用於支付利息）
        initial_balance_reduction = config.principal - remaining_balances[2]  # 寬限期內的本金減少
        later_balance_reduction = remaining_balances[5] - remaining_balances[8]  # 寬限期後同樣期間的本金減少
        
        # 寬限期後的本金減少速度應該更快
        assert later_balance_reduction > initial_balance_reduction

    def test_with_interest_changes(self):
        """測試利率變動的攤銷表計算
        
        測試利率變動情況下的攤銷表計算，驗證以下重點：
        1. 利率變動前後的利息計算是否正確
        2. 利率變動是否在指定日期生效
        """
        # 設定利率變動情況
        interest_changes = [
            InterestChange(
                effective_date=datetime(2023, 7, 1),
                new_rate=0.042,  # 從 3.6% 變更為 4.2%
                description="央行調升基準利率"
            )
        ]
        
        # 設定貸款參數
        config = LoanConfig(
            principal=1000000,
            periods=12,
            annual_rate=0.036,
            start_date=datetime(2023, 1, 1),
            method=Method.EQUAL_PAYMENT,
            interest_changes=interest_changes
        )
        
        # 使用函數計算攤銷表
        result_df = calculate_loan_amortization(config)
        
        # 提取結果數據
        interest_expenses = result_df["利息費用"].to_list()
        
        # 驗證利率變動前後的利息費用差異
        # 第 5 期（6 月）使用舊利率
        june_interest = interest_expenses[5]
        # 第 6 期（7 月）使用新利率
        july_interest = interest_expenses[6]
        
        # 假設本金接近，利息費用應因利率上升而增加
        # 注意：實際上 7 月的本金會比 6 月少，所以我們需要估計這個差異
        # 但在短期內，利率變動的影響應該比本金減少的影響更顯著
        # 估算 7 月的利息如果使用舊利率
        july_principal = result_df["期初金額"].to_list()[6]
        estimated_july_interest_old_rate = july_principal * (0.036 / 12)
        estimated_july_interest_new_rate = july_principal * (0.042 / 12)
        
        # 利率變動的影響應該顯著
        assert abs(estimated_july_interest_new_rate - estimated_july_interest_old_rate) > 0
        # 實際 7 月利息應接近使用新利率的估計值
        assert abs(july_interest - estimated_july_interest_new_rate) < 1

    def test_payment_type(self):
        """測試不同付款類型（月初或月底）的影響
        
        驗證月初付款和月底付款的還款日期差異
        """
        # 設定貸款參數（月初付款）
        config_begin = LoanConfig(
            principal=1000000,
            periods=12,
            annual_rate=0.036,
            start_date=datetime(2023, 1, 15),
            payment_type=PaymentType.BEGIN
        )
        
        # 設定貸款參數（月底付款）
        config_end = LoanConfig(
            principal=1000000,
            periods=12,
            annual_rate=0.036,
            start_date=datetime(2023, 1, 15),
            payment_type=PaymentType.END
        )
        
        # 計算兩種付款類型的攤銷表
        result_begin = calculate_loan_amortization(config_begin)
        result_end = calculate_loan_amortization(config_end)
        
        # 提取付款日期
        dates_begin = result_begin["還款日期"].to_list()
        dates_end = result_end["還款日期"].to_list()
        
        # 驗證月底付款日期是當月最後一天
        assert dates_end[0].day == 31  # 1月有31天
        assert dates_end[1].day == 28  # 2023年2月有28天
        
        # 驗證月初付款日期保持不變
        assert dates_begin[0].day == 15
        assert dates_begin[1].day == 15

    def test_different_interest_periods(self):
        """測試不同計息週期的影響
        
        驗證不同計息週期（月、季、半年、年）的利息計算差異
        """
        # 基本貸款設定
        base_config = {
            "principal": 1000000,
            "periods": 24,
            "annual_rate": 0.036,
            "start_date": datetime(2023, 1, 1)
        }
        
        # 建立不同計息週期的設定
        monthly_config = LoanConfig(**base_config, interest_period=InterestPeriod.MONTHLY)
        quarterly_config = LoanConfig(**base_config, interest_period=InterestPeriod.QUARTERLY)
        half_yearly_config = LoanConfig(**base_config, interest_period=InterestPeriod.HALF_YEARLY)
        yearly_config = LoanConfig(**base_config, interest_period=InterestPeriod.YEARLY)
        
        # 計算各計息週期的攤銷表
        monthly_result = calculate_loan_amortization(monthly_config)
        quarterly_result = calculate_loan_amortization(quarterly_config)
        half_yearly_result = calculate_loan_amortization(half_yearly_config)
        yearly_result = calculate_loan_amortization(yearly_config)
        
        # 提取利息費用資料
        monthly_interest = monthly_result["利息費用"].to_list()
        quarterly_interest = quarterly_result["利息費用"].to_list()
        half_yearly_interest = half_yearly_result["利息費用"].to_list()
        yearly_interest = yearly_result["利息費用"].to_list()
        
        # 驗證不同計息週期的利息頻率
        # 月計息：每期都有利息
        assert all(interest > 0 for interest in monthly_interest[:12])
        
        # 季計息：每季（3個月）才有一次利息，其他期間利息為0
        assert quarterly_interest[0] > 0  # 第1期（計息期）
        assert quarterly_interest[1] == 0  # 第2期（非計息期）
        assert quarterly_interest[2] == 0  # 第3期（非計息期）
        assert quarterly_interest[3] > 0  # 第4期（計息期）
        
        # 半年計息：每半年（6個月）才有一次利息
        assert half_yearly_interest[0] > 0  # 第1期（計息期）
        assert all(interest == 0 for interest in half_yearly_interest[1:5])  # 第2-6期（非計息期）
        assert half_yearly_interest[6] > 0  # 第7期（計息期）
        
        # 年計息：每年（12個月）才有一次利息
        assert yearly_interest[0] > 0  # 第1期（計息期）
        assert all(interest == 0 for interest in yearly_interest[1:11])  # 第2-12期（非計息期）
        assert yearly_interest[12] > 0  # 第13期（計息期）

    def test_fees_calculation(self):
        """測試費用計算
        
        驗證各種費用（服務費、開辦費、帳戶管理費、保證手續費）的計算
        """
        # 設定費用
        fees = Fees(
            service_fee_rate=0.005,         # 0.5% 服務費率
            account_management_fee=100,     # 每期 100 元帳戶管理費
            setup_fee=5000,                 # 5000 元開辦費
            guarantee_fee_rate=0.002,       # 0.2% 保證手續費率
            late_payment_penalty_rate=0.1   # 10% 逾期違約金率（未使用）
        )
        
        # 設定貸款參數
        config = LoanConfig(
            principal=1000000,
            periods=12,
            annual_rate=0.036,
            start_date=datetime(2023, 1, 1),
            fees=fees
        )
        
        # 計算攤銷表
        result = calculate_loan_amortization(config)
        
        # 提取費用資料
        service_fees = result["服務費"].to_list()
        account_fees = result["帳戶管理費"].to_list()
        guarantee_fees = result["保證手續費"].to_list()
        total_fees = result["總費用"].to_list()
        
        # 驗證第一期費用（含開辦費）
        expected_service_fee_first = 1000000 * 0.005 / 12
        expected_guarantee_fee_first = 1000000 * 0.002 / 12
        expected_account_fee = 100
        expected_total_first = expected_service_fee_first + expected_guarantee_fee_first + expected_account_fee + 5000
        
        assert abs(service_fees[0] - expected_service_fee_first) < 0.01
        assert account_fees[0] == expected_account_fee
        assert abs(guarantee_fees[0] - expected_guarantee_fee_first) < 0.01
        assert abs(total_fees[0] - expected_total_first) < 0.01
        
        # 驗證第二期費用（不含開辦費）
        expected_total_second = expected_service_fee_first + expected_guarantee_fee_first + expected_account_fee
        # 由於本金減少，第二期的服務費和保證手續費應略低於第一期
        assert service_fees[1] < service_fees[0]
        assert guarantee_fees[1] < guarantee_fees[0]
        # 帳戶管理費應維持不變
        assert account_fees[1] == expected_account_fee
        # 第二期總費用應顯著低於第一期（因為沒有開辦費）
        assert total_fees[1] < total_fees[0] - 4000

    def test_different_payment_frequencies(self):
        """測試不同還款頻率
        
        驗證不同還款頻率（月付、雙週付、週付）的還款計算差異
        """
        # 基本貸款設定
        base_config = {
            "principal": 1000000,
            "annual_rate": 0.036,
            "start_date": datetime(2023, 1, 1)
        }
        
        # 建立不同還款頻率的設定（調整期數以保持相似的總還款時間）
        monthly_config = LoanConfig(**base_config, periods=12, payment_frequency=PaymentFrequency.MONTHLY)
        biweekly_config = LoanConfig(**base_config, periods=26, payment_frequency=PaymentFrequency.BIWEEKLY)
        weekly_config = LoanConfig(**base_config, periods=52, payment_frequency=PaymentFrequency.WEEKLY)
        
        # 計算各還款頻率的攤銷表
        monthly_result = calculate_loan_amortization(monthly_config)
        biweekly_result = calculate_loan_amortization(biweekly_config)
        weekly_result = calculate_loan_amortization(weekly_config)
        
        # 提取還款日期和還款金額
        monthly_dates = monthly_result["還款日期"].to_list()
        biweekly_dates = biweekly_result["還款日期"].to_list()
        weekly_dates = weekly_result["還款日期"].to_list()
        
        monthly_payments = monthly_result["每期支付額"].to_list()
        biweekly_payments = biweekly_result["每期支付額"].to_list()
        weekly_payments = weekly_result["每期支付額"].to_list()
        
        # 驗證還款日期間隔
        assert (monthly_dates[1] - monthly_dates[0]).days >= 28  # 月付間隔約一個月
        assert (biweekly_dates[1] - biweekly_dates[0]).days == 14  # 雙週付間隔14天
        assert (weekly_dates[1] - weekly_dates[0]).days == 7  # 週付間隔7天
        
        # 驗證還款金額（週付<雙週付<月付）
        assert weekly_payments[0] < biweekly_payments[0]
        assert biweekly_payments[0] < monthly_payments[0]
        
        # 驗證總還款金額接近（考慮浮點數誤差）
        monthly_total = sum(monthly_payments)
        biweekly_total = sum(biweekly_payments)
        weekly_total = sum(weekly_payments)
        
        # 由於還款頻率不同，總還款額會有差異，但應在合理範圍內
        assert abs(monthly_total - biweekly_total) / monthly_total < 0.05
        assert abs(monthly_total - weekly_total) / monthly_total < 0.05

    def test_no_fees_and_no_grace_period_case(self):
        """測試無費用和無寬限期的情況
        
        測試無費用設定和無寬限期時的攤銷表計算
        """
        # 設定貸款參數（無費用、無寬限期）
        config = LoanConfig(
            principal=1000000,
            periods=12,
            annual_rate=0.036,
            start_date=datetime(2023, 1, 1),
            fees=None,
            grace_period=None
        )
        
        # 計算攤銷表
        result = calculate_loan_amortization(config)
        
        # 驗證費用欄位全為零
        service_fees = result["服務費"].to_list()
        account_fees = result["帳戶管理費"].to_list()
        guarantee_fees = result["保證手續費"].to_list()
        total_fees = result["總費用"].to_list()
        
        assert all(fee == 0 for fee in service_fees)
        assert all(fee == 0 for fee in account_fees)
        assert all(fee == 0 for fee in guarantee_fees)
        assert all(fee == 0 for fee in total_fees)
        
        # 驗證每期支付額等於本金償還加利息費用
        payments = result["每期支付額"].to_list()
        principal_repayments = result["本金償還"].to_list()
        interest_expenses = result["利息費用"].to_list()
        
        for i in range(len(payments)):
            assert abs(payments[i] - (principal_repayments[i] + interest_expenses[i])) < 0.01

    def test_equal_principal_with_grace_period(self):
        """測試本金平均攤還法（等額本金）與寬限期的組合
        
        測試本金平均攤還法與寬限期結合時的還款計算
        """
        # 建立寬限期物件
        grace_period = GracePeriod()
        grace_period.months = 3
        
        # 設定貸款參數
        config = LoanConfig(
            principal=1000000,
            periods=12,
            annual_rate=0.036,
            start_date=datetime(2023, 1, 1),
            method=Method.EQUAL_PRINCIPAL,  # 使用本金平均攤還法
            grace_period=grace_period
        )
        
        # 使用函數計算攤銷表
        result_df = calculate_loan_amortization(config)
        
        # 提取結果數據
        principal_repayments = result_df["本金償還"].to_list()
        
        # 驗證寬限期內和寬限期後的本金償還金額相同（等額本金的特性）
        assert abs(principal_repayments[0] - principal_repayments[5]) < 0.01 