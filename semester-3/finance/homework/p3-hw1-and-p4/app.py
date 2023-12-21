import numpy as np
import streamlit as st
import pandas as pd

from requests import Session
from requests_cache import CacheMixin, SQLiteCache
from requests_ratelimiter import LimiterMixin, MemoryQueueBucket
from pyrate_limiter import Duration, RequestRate, Limiter
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
from algorithms import first_algorithm, portfolio_algorithm

class CachedLimiterSession(CacheMixin, LimiterMixin, Session):
    pass

session = CachedLimiterSession(
    limiter=Limiter(RequestRate(2, Duration.SECOND*5)),  # max 2 requests per 5 seconds
    bucket_class=MemoryQueueBucket,
    backend=SQLiteCache("yfinance.cache"),
)
session.headers['User-agent'] = 'n.finance/1.0'

"# 任選股票建構投資組合，這裡會顯示投資組合的累積報酬率"

"## 選擇股票"
stocks = st.multiselect("選擇股票", ["2201.TW", "2330.TW", "2888.TW", "2317.TW", "2603.TW", "2327.TW", "2371.TW", "1314.TW", "2409.TW", "0050.TW", "2881.TW"])
tickers = yf.Tickers(stocks, session=session)

if len(stocks) < 2:
    st.write("請至少選擇兩支股票")
    st.stop()

"## 選擇時間區間"
start_date = st.date_input("開始日期", value=pd.to_datetime("2014-01-01"))
end_date = st.date_input("結束日期", value=pd.to_datetime("2016-12-31"))

# 取回資料
close = tickers.history(start=start_date, end=end_date, auto_adjust=False)["Close"]
ret = close.pct_change(fill_method=None)

col1, col2 = st.columns(2)

with col1:
    "## 計算投資比例"
    methods = st.radio("權重計算方式", ["馬可維茲", "首筆算法"])
    weight: pd.Series | None = None

    match methods:
        case "首筆算法":
            count = pd.Series([st.slider(stock, 0, 100, value=1) for stock in stocks], index=stocks, dtype=int)
            weight = first_algorithm(close, count)
        case "馬可維茲":
            expected_ret_rate = st.slider("目標報酬率", 0.0, 1.0, value=0.006, step=0.1**8, format="%.8f")
            weight = portfolio_algorithm(close, float(expected_ret_rate))
with col2:
    "## 資產配置"
    fig, ax = plt.subplots()
    ax.pie(weight, labels=stocks, autopct="%1.1f%%")
    st.pyplot(fig)

    "## 累積收益率圖"
    fig, ax = plt.subplots()
    cumret = (1 + ret).cumprod() - 1
    for stock in stocks:
        ax.plot(cumret[stock], label=stock)
    ax.legend()
    st.pyplot(fig)


"## 數據"
assert weight is not None

rewards = np.sum(ret.mean() * weight)
var = np.sum((weight ** 2) * ret.var())

for i in range(0, len(stocks)):
    for j in range(i + 1, len(stocks)):
        s1 = stocks[i]
        s2 = stocks[j]

        w1 = weight[s1]
        w2 = weight[s2]

        var += w1*w2 * ret[s1].cov(ret[s2])

st.json({
    "報酬率": rewards,
    "風險": var,
})

# mu = expected_returns.mean_historical_return(train_set)
# historical_returns = expected_returns.returns_from_prices(train_set)
