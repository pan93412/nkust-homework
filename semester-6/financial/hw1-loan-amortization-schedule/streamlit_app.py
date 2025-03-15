import streamlit as st
from datetime import datetime
from structure import (
    LoanConfig, Method, PaymentFrequency,
    PaymentType, InterestPeriod, GracePeriod,
    PrepaymentOptions, Fees
)
from calculate import calculate_loan_amortization

st.set_page_config(
    page_title="貸款攤銷表計算器",
    page_icon="💰",
    layout="wide"
)

st.title("貸款攤銷表計算器 💰")

# 建立側邊欄以輸入貸款設定
with st.sidebar:
    st.header("貸款設定")
    
    # 使用 tabs 來組織不同類別的設定
    basic_tab, advanced_tab = st.tabs(["基本設定", "進階設定"])
    
    with basic_tab:
        # 基本貸款資訊
        principal = st.number_input(
            "貸款金額（元）",
            min_value=1,
            value=1000000,
            step=10000,
            format="%d"
        )
        
        periods = st.number_input(
            "貸款期數（月）",
            min_value=1,
            value=24,
            step=1,
            format="%d"
        )
        
        annual_rate = st.number_input(
            "年利率（%）",
            min_value=0.0,
            value=2.5,
            step=0.1,
            format="%.2f"
        ) / 100  # 轉換為小數
        
        start_date = st.date_input(
            "貸款起始日期",
            value=datetime.now()
        )
        
        # 還款方式設定
        method = st.selectbox(
            "攤還方法",
            options=[Method.EQUAL_PAYMENT, Method.EQUAL_PRINCIPAL],
            format_func=str
        )
        
        payment_frequency = st.selectbox(
            "還款頻率",
            options=[
                PaymentFrequency.MONTHLY,
                PaymentFrequency.BIWEEKLY,
                PaymentFrequency.WEEKLY
            ],
            format_func=str
        )
        
        payment_type = st.selectbox(
            "付款時間",
            options=[PaymentType.END, PaymentType.BEGIN],
            format_func=str
        )
    
    with advanced_tab:
        # 利息計算設定
        interest_period = st.selectbox(
            "計息頻率",
            options=[
                InterestPeriod.MONTHLY,
                InterestPeriod.QUARTERLY,
                InterestPeriod.HALF_YEARLY,
                InterestPeriod.YEARLY
            ],
            format_func=lambda x: f"每 {x.value} 個月"
        )
        
        # 寬限期設定
        has_grace_period = st.checkbox("設定寬限期")
        grace_period = None
        if has_grace_period:
            grace_months = st.number_input(
                "寬限期（月）",
                min_value=1,
                value=6,
                step=1
            )
            grace_period = GracePeriod()
            grace_period.months = grace_months
        
        # 提前還款選項
        has_prepayment = st.checkbox("設定提前還款選項")
        prepayment_options = None
        if has_prepayment:
            with st.expander("提前還款設定"):
                min_amount = st.number_input(
                    "最低提前還款金額",
                    min_value=0,
                    value=10000,
                    step=1000
                )
                penalty_rate = st.number_input(
                    "提前還款違約金率（%）",
                    min_value=0.0,
                    value=2.0,
                    step=0.1
                ) / 100
                allow_partial = st.checkbox("允許部分提前還款", value=True)
                penalty_period = st.number_input(
                    "違約金收取期間（月）",
                    min_value=0,
                    value=12,
                    step=1
                )
                prepayment_options = PrepaymentOptions(
                    min_amount=min_amount,
                    penalty_rate=penalty_rate,
                    allow_partial=allow_partial,
                    penalty_period=penalty_period
                )
        
        # 費用設定
        has_fees = st.checkbox("設定相關費用")
        fees = None
        if has_fees:
            with st.expander("費用設定"):
                service_fee = st.number_input(
                    "服務費率（年率%）",
                    min_value=0.0,
                    value=0.5,
                    step=0.1
                ) / 100
                late_fee = st.number_input(
                    "逾期違約金率（年率%）",
                    min_value=0.0,
                    value=5.0,
                    step=0.1
                ) / 100
                account_fee = st.number_input(
                    "帳戶管理費（每期）",
                    min_value=0.0,
                    value=100.0,
                    step=10.0
                )
                setup_fee = st.number_input(
                    "開辦費",
                    min_value=0.0,
                    value=5000.0,
                    step=1000.0
                )
                guarantee_fee = st.number_input(
                    "保證手續費率（年率%）",
                    min_value=0.0,
                    value=0.5,
                    step=0.1
                ) / 100
                fees = Fees(
                    service_fee_rate=service_fee,
                    late_payment_penalty_rate=late_fee,
                    account_management_fee=account_fee,
                    setup_fee=setup_fee,
                    guarantee_fee_rate=guarantee_fee
                )

# 建立貸款設定物件
loan_config = LoanConfig(
    principal=principal,
    periods=periods,
    annual_rate=annual_rate,
    start_date=datetime.combine(start_date, datetime.min.time()),
    payment_type=payment_type,
    method=method,
    payment_frequency=payment_frequency,
    interest_period=interest_period,
    grace_period=grace_period,
    prepayment_options=prepayment_options,
    fees=fees
)

# 顯示貸款設定摘要
st.subheader("貸款設定摘要")

# 使用卡片式布局顯示設定摘要
col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 基本資訊")
    st.markdown(f"""
    - 💵 貸款金額：**{principal:,}** 元
    - 📅 期數：**{periods}** 期
    - 💹 年利率：**{annual_rate * 100:.2f}**%
    - 📆 開始日期：**{start_date.strftime('%Y年%m月%d日')}**
    """)
    
    st.markdown("#### 還款設定")
    st.markdown(f"""
    - 📊 還款方式：**{method}**
    - 🔄 還款頻率：**{payment_frequency}**
    - ⏰ 付款時間：**{payment_type}**
    - 📈 計息頻率：**每 {interest_period.value} 個月**
    """)

with col2:
    if grace_period:
        st.markdown("#### 寬限期設定")
        st.markdown(f"- ⏳ 寬限期：**{grace_period}**")
    
    if prepayment_options:
        st.markdown("#### 提前還款設定")
        st.markdown(f"""
        - 💰 最低金額：**{prepayment_options.min_amount:,}** 元
        - 📊 違約金率：**{prepayment_options.penalty_rate * 100:.2f}**%
        - ✅ 允許部分還款：**{'是' if prepayment_options.allow_partial else '否'}**
        - ⏳ 違約金期間：**{prepayment_options.penalty_period}** 個月
        """)
    
    if fees:
        st.markdown("#### 費用設定")
        st.markdown(f"""
        - 💼 服務費率：**{fees.service_fee_rate * 100:.2f}**%/年
        - ⚠️ 逾期違約金率：**{fees.late_payment_penalty_rate * 100:.2f}**%/年
        - 💳 帳戶管理費：**{fees.account_management_fee:,.2f}** 元/期
        - 📝 開辦費：**{fees.setup_fee:,.2f}** 元
        - 🔒 保證手續費率：**{fees.guarantee_fee_rate * 100:.2f}**%/年
        """)

# 計算並顯示攤銷表
st.subheader("攤銷表")
df = calculate_loan_amortization(loan_config)

# 轉換為 Pandas DataFrame 以便 Streamlit 顯示
pd_df = df.to_pandas()

# 設定數值格式
pd_df = pd_df.round(2)
# 格式化日期
pd_df["還款日期"] = pd_df["還款日期"].dt.strftime("%Y年%m月%d日")
# 格式化金額
for col in ["期初金額", "每期支付額", "利息費用", "本金償還", "期末欠款"]:
    pd_df[col] = pd_df[col].apply(lambda x: f"{x:,.2f}")

st.dataframe(
    pd_df,
    use_container_width=True,
    hide_index=True
)

# 顯示統計資訊
st.subheader("統計資訊")
col1, col2, col3 = st.columns(3)

total_payment = df["每期支付額"].sum()
total_interest = df["利息費用"].sum()
total_principal = df["本金償還"].sum()

with col1:
    st.metric("總支付金額", f"{total_payment:,.2f} 元")
with col2:
    st.metric("總利息支出", f"{total_interest:,.2f} 元")
with col3:
    st.metric("實際本金", f"{total_principal:,.2f} 元")
