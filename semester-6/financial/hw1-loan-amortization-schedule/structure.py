from enum import Enum
from dataclasses import dataclass
from datetime import datetime


class PaymentType(Enum):
    END = "end"
    BEGIN = "begin"

    def __str__(self) -> str:
        chinese_type = {
            PaymentType.END: "月底",
            PaymentType.BEGIN: "月初"
        }

        return chinese_type[self]


class Method(Enum):
    EQUAL_PAYMENT = "equal_payment"
    EQUAL_PRINCIPAL = "equal_principal"

    def __str__(self) -> str:
        chinese_type = {
            Method.EQUAL_PAYMENT: "本息平均攤還",
            Method.EQUAL_PRINCIPAL: "本金平均攤還"
        }

        return chinese_type[self]


class PaymentFrequency(Enum):
    MONTHLY = "monthly"
    BIWEEKLY = "biweekly"
    WEEKLY = "weekly"

    def __str__(self) -> str:
        chinese_type = {
            PaymentFrequency.MONTHLY: "每月",
            PaymentFrequency.BIWEEKLY: "每雙週",
            PaymentFrequency.WEEKLY: "每周"
        }

        return chinese_type[self]


class GracePeriod:
    """寬限期"""
    months: int

    def __repr__(self) -> str:
        return f"{self.months} 個月"


class InterestPeriod(Enum):
    MONTHLY = 1
    QUARTERLY = 3
    HALF_YEARLY = 6
    YEARLY = 12


@dataclass
class InterestChange:
    """利率變動資訊"""
    effective_date: datetime  # 生效日期
    new_rate: float  # 新年利率（如 0.018 表示 1.8%）
    description: str | None = None  # 變動原因描述（選填）


@dataclass
class PrepaymentOptions:
    """提前還款選項"""
    min_amount: int = 0  # 最低提前還款金額
    penalty_rate: float = 0.0  # 提前還款違約金率（如 0.02 表示 2%）
    allow_partial: bool = True  # 是否允許部分提前還款
    penalty_period: int = 0  # 收取違約金的期間（月），0 表示無期限


@dataclass
class Fees:
    """貸款相關費用"""
    service_fee_rate: float = 0.0  # 服務費率（年率）
    late_payment_penalty_rate: float = 0.0  # 逾期違約金率（年率）
    account_management_fee: float = 0.0  # 帳戶管理費（每期）
    setup_fee: float = 0.0  # 開辦費
    guarantee_fee_rate: float = 0.0  # 保證手續費率（年率）


@dataclass
class LoanConfig:
    """貸款設定"""
    # 基本貸款資訊
    principal: int  # 貸款總額
    periods: int  # 貸款期數（月）
    annual_rate: float  # 年利率（如 0.018 表示 1.8%）
    start_date: datetime  # 貸款起始日期
    
    # 還款方式設定
    payment_type: PaymentType = PaymentType.END  # 付款方式
    method: Method = Method.EQUAL_PAYMENT  # 攤還方法
    payment_frequency: PaymentFrequency = PaymentFrequency.MONTHLY  # 還款頻率
    
    # 利息計算設定
    interest_period: InterestPeriod = InterestPeriod.MONTHLY  # 計息頻率
    interest_changes: list[InterestChange] | None = None  # 利率變動記錄
    
    # 寬限期設定
    grace_period: GracePeriod | None = None  # 寬限期
    
    # 其他選項
    prepayment_options: PrepaymentOptions | None = None  # 提前還款選項
    fees: Fees | None = None  # 費用設定

    def __repr__(self) -> str:
        """產生貸款設定的中文摘要說明"""
        return f"""
貸款基本資訊：
- 貸款金額：{self.principal:,} 元
- 期數：{self.periods} 期
- 年利率：{self.annual_rate * 100:.2f}%
- 開始日期：{self.start_date.strftime('%Y年%m月%d日')}
- 還款方式：{self.method}
- 還款頻率：{self.payment_frequency}

計息設定：
- 計息週期：{self.interest_period.value} 個月
- 利率異動：{'有' if self.interest_changes else '無'}

寬限期設定：
- 寬限期：{self.grace_period if self.grace_period else '沒有寬限期'}

其他設定：
- 提前還款選項：{'有' if self.prepayment_options else '無'}
- 費用設定：{'有' if self.fees else '無'}
"""
