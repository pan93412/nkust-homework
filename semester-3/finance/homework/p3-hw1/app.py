import streamlit as st
import pandas as pd

from requests import Session
from requests_cache import CacheMixin, SQLiteCache
from requests_ratelimiter import LimiterMixin, MemoryQueueBucket
from pyrate_limiter import Duration, RequestRate, Limiter
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf

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
stocks = st.multiselect("選擇股票", ["2201.TW", "2330.TW", "2888.TW", "2317.TW", "2603.TW", "2327.TW", "2371.TW", "1314.TW", "2409.TW", "0050.TW"])
tickers = yf.Tickers(stocks, session=session)

"## 選擇時間區間"
start_date = st.date_input("開始日期", value=pd.to_datetime("2014-01-01"))
end_date = st.date_input("結束日期", value=pd.to_datetime("2016-12-31"))

# 取回資料
close = tickers.history(start=start_date, end=end_date, auto_adjust=False)["Close"]
ret = close.pct_change(fill_method=None)

"## 選擇股票張數"

count = [st.slider(stock, 0, 100, value=1) for stock in stocks]

"## 選擇投資比例"

total = sum([c * r for c, r in zip(count, close.iloc[0])])
weight = [
    (c * r) / total
    for c, r in zip(count, close.iloc[0])
]

col1, col2 = st.columns(2)

with col1:
    st.dataframe(pd.DataFrame({
        "張數": count,
        "比例": weight
    }, index=stocks), use_container_width=True)

with col2:
    fig, ax = plt.subplots()
    ax.pie(weight, labels=stocks, autopct="%1.1f%%")
    st.pyplot(fig)

"## 數據"

rewards = 0
var = 0

for i, stock in enumerate(stocks):
    rewards += ret[stock].mean() * weight[i]

    var *= weight[i]**2 * ret[stock].std()**2


st.write(f"- 報酬: {round(rewards * 100, 4)}%")

