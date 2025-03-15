import pytest
from datetime import datetime

from structure import (
    PaymentType, Method, PaymentFrequency, InterestPeriod,
    GracePeriod, InterestChange, PrepaymentOptions, Fees, LoanConfig
)


class TestEnums:
    """測試枚舉類型的正確性"""

    def test_payment_type_enum(self):
        """測試付款方式枚舉
        
        測試 PaymentType 枚舉的值和字串表示是否正確。
        """
        # 驗證枚舉值
        assert PaymentType.END.value == "end"
        assert PaymentType.BEGIN.value == "begin"
        
        # 驗證字串表示
        assert str(PaymentType.END) == "月底"
        assert str(PaymentType.BEGIN) == "月初"

    def test_method_enum(self):
        """測試攤還方法枚舉
        
        測試 Method 枚舉的值和字串表示是否正確。
        """
        # 驗證枚舉值
        assert Method.EQUAL_PAYMENT.value == "equal_payment"
        assert Method.EQUAL_PRINCIPAL.value == "equal_principal"
        
        # 驗證字串表示
        assert str(Method.EQUAL_PAYMENT) == "本息平均攤還"
        assert str(Method.EQUAL_PRINCIPAL) == "本金平均攤還"

    def test_payment_frequency_enum(self):
        """測試還款頻率枚舉
        
        測試 PaymentFrequency 枚舉的值和字串表示是否正確。
        """
        # 驗證枚舉值
        assert PaymentFrequency.MONTHLY.value == "monthly"
        assert PaymentFrequency.BIWEEKLY.value == "biweekly"
        assert PaymentFrequency.WEEKLY.value == "weekly"
        
        # 驗證字串表示
        assert str(PaymentFrequency.MONTHLY) == "每月"
        assert str(PaymentFrequency.BIWEEKLY) == "每雙週"
        assert str(PaymentFrequency.WEEKLY) == "每周"

    def test_interest_period_enum(self):
        """測試計息頻率枚舉
        
        測試 InterestPeriod 枚舉的值是否符合實際月數。
        """
        # 驗證枚舉值（對應月數）
        assert InterestPeriod.MONTHLY.value == 1
        assert InterestPeriod.QUARTERLY.value == 3
        assert InterestPeriod.HALF_YEARLY.value == 6
        assert InterestPeriod.YEARLY.value == 12


class TestGracePeriod:
    """測試寬限期類別"""

    def test_grace_period_representation(self):
        """測試寬限期類別的字串表示
        
        驗證 GracePeriod 的 __repr__ 方法是否正確顯示寬限期的月數。
        """
        # 建立寬限期物件
        grace_period = GracePeriod()
        grace_period.months = 6
        
        # 驗證字串表示
        assert repr(grace_period) == "6 個月"


class TestDataClasses:
    """測試數據類別的功能"""

    def test_interest_change_creation(self):
        """測試利率變動資訊類別
        
        測試 InterestChange 資料類別的創建和屬性是否正確。
        """
        # 建立利率變動物件
        effective_date = datetime(2023, 7, 1)
        new_rate = 0.042
        description = "央行調升基準利率"
        
        interest_change = InterestChange(
            effective_date=effective_date,
            new_rate=new_rate,
            description=description
        )
        
        # 驗證屬性
        assert interest_change.effective_date == effective_date
        assert interest_change.new_rate == new_rate
        assert interest_change.description == description
        
        # 測試沒有描述的情況
        interest_change_no_desc = InterestChange(
            effective_date=effective_date,
            new_rate=new_rate
        )
        
        assert interest_change_no_desc.description is None

    def test_prepayment_options_defaults(self):
        """測試提前還款選項類別的預設值
        
        測試 PrepaymentOptions 資料類別的預設值是否符合預期。
        """
        # 使用預設值建立物件
        prepayment_options = PrepaymentOptions()
        
        # 驗證預設值
        assert prepayment_options.min_amount == 0
        assert prepayment_options.penalty_rate == 0.0
        assert prepayment_options.allow_partial == True
        assert prepayment_options.penalty_period == 0
        
        # 測試自訂值
        custom_options = PrepaymentOptions(
            min_amount=10000,
            penalty_rate=0.02,
            allow_partial=False,
            penalty_period=12
        )
        
        assert custom_options.min_amount == 10000
        assert custom_options.penalty_rate == 0.02
        assert custom_options.allow_partial == False
        assert custom_options.penalty_period == 12

    def test_fees_defaults(self):
        """測試費用類別的預設值
        
        測試 Fees 資料類別的預設值是否符合預期。
        """
        # 使用預設值建立物件
        fees = Fees()
        
        # 驗證預設值
        assert fees.service_fee_rate == 0.0
        assert fees.late_payment_penalty_rate == 0.0
        assert fees.account_management_fee == 0.0
        assert fees.setup_fee == 0.0
        assert fees.guarantee_fee_rate == 0.0
        
        # 測試自訂值
        custom_fees = Fees(
            service_fee_rate=0.005,
            late_payment_penalty_rate=0.02,
            account_management_fee=100,
            setup_fee=5000,
            guarantee_fee_rate=0.01
        )
        
        assert custom_fees.service_fee_rate == 0.005
        assert custom_fees.late_payment_penalty_rate == 0.02
        assert custom_fees.account_management_fee == 100
        assert custom_fees.setup_fee == 5000
        assert custom_fees.guarantee_fee_rate == 0.01


class TestLoanConfig:
    """測試貸款設定類別"""

    def test_loan_config_required_fields(self):
        """測試貸款設定必填欄位
        
        測試 LoanConfig 類別必填欄位的設定是否正確。
        """
        # 設定必填欄位
        principal = 1000000
        periods = 12
        annual_rate = 0.036
        start_date = datetime(2023, 1, 1)
        
        # 使用必填欄位建立貸款設定
        config = LoanConfig(
            principal=principal,
            periods=periods,
            annual_rate=annual_rate,
            start_date=start_date
        )
        
        # 驗證必填欄位
        assert config.principal == principal
        assert config.periods == periods
        assert config.annual_rate == annual_rate
        assert config.start_date == start_date
        
        # 驗證預設值
        assert config.payment_type == PaymentType.END
        assert config.method == Method.EQUAL_PAYMENT
        assert config.payment_frequency == PaymentFrequency.MONTHLY
        assert config.interest_period == InterestPeriod.MONTHLY
        assert config.interest_changes is None
        assert config.grace_period is None
        assert config.prepayment_options is None
        assert config.fees is None

    def test_loan_config_all_fields(self):
        """測試貸款設定全部欄位
        
        測試 LoanConfig 類別全部欄位的設定是否正確。
        """
        # 設定必填欄位
        principal = 1000000
        periods = 12
        annual_rate = 0.036
        start_date = datetime(2023, 1, 1)
        
        # 設定選填欄位
        payment_type = PaymentType.BEGIN
        method = Method.EQUAL_PRINCIPAL
        payment_frequency = PaymentFrequency.BIWEEKLY
        interest_period = InterestPeriod.QUARTERLY
        
        # 設定利率變動
        interest_changes = [
            InterestChange(
                effective_date=datetime(2023, 7, 1),
                new_rate=0.042,
                description="央行調升基準利率"
            )
        ]
        
        # 設定寬限期
        grace_period = GracePeriod()
        grace_period.months = 3
        
        # 設定提前還款選項
        prepayment_options = PrepaymentOptions(
            min_amount=10000,
            penalty_rate=0.02,
            allow_partial=False,
            penalty_period=6
        )
        
        # 設定費用
        fees = Fees(
            service_fee_rate=0.005,
            late_payment_penalty_rate=0.02,
            account_management_fee=100,
            setup_fee=5000,
            guarantee_fee_rate=0.01
        )
        
        # 建立完整的貸款設定
        config = LoanConfig(
            principal=principal,
            periods=periods,
            annual_rate=annual_rate,
            start_date=start_date,
            payment_type=payment_type,
            method=method,
            payment_frequency=payment_frequency,
            interest_period=interest_period,
            interest_changes=interest_changes,
            grace_period=grace_period,
            prepayment_options=prepayment_options,
            fees=fees
        )
        
        # 驗證必填欄位
        assert config.principal == principal
        assert config.periods == periods
        assert config.annual_rate == annual_rate
        assert config.start_date == start_date
        
        # 驗證選填欄位
        assert config.payment_type == payment_type
        assert config.method == method
        assert config.payment_frequency == payment_frequency
        assert config.interest_period == interest_period
        assert config.interest_changes == interest_changes
        assert config.grace_period == grace_period
        assert config.prepayment_options == prepayment_options
        assert config.fees == fees

    def test_loan_config_representation(self):
        """測試貸款設定的字串表示
        
        測試 LoanConfig 的 __repr__ 方法是否正確生成貸款摘要說明。
        """
        # 建立基本貸款設定
        config = LoanConfig(
            principal=1000000,
            periods=12,
            annual_rate=0.036,
            start_date=datetime(2023, 1, 1)
        )
        
        # 獲取字串表示
        representation = repr(config)
        
        # 驗證重要資訊是否包含在字串表示中
        assert "貸款金額：1,000,000 元" in representation
        assert "期數：12 期" in representation
        assert "年利率：3.60%" in representation
        assert "2023年01月01日" in representation
        assert "還款方式：本息平均攤還" in representation
        assert "還款頻率：每月" in representation 