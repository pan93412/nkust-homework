from datetime import datetime

from calculate import calculate_payment_amount, get_payment_dates, calculate_loan_amortization
from structure import LoanConfig, Method, PaymentFrequency, GracePeriod, InterestChange


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