import streamlit as st
from sources.yfinance import YahooFinanceFetcher
import statsmodels.api as sm

fetcher = YahooFinanceFetcher()
tickers = fetcher.get_tickers(["TSM", "2409.TW"]).history(start='2022-01-01', end='2022-12-31', auto_adjust=False)
close = tickers['Close'].dropna()

tsm_adr_close = close["TSM"]
auo_close = close["2409.TW"]

st.dataframe(tsm_adr_close)
st.dataframe(auo_close)

regression = sm.OLS(auo_close, sm.add_constant(tsm_adr_close)).fit()
st.markdown("## Regression for AUO compared to TSM")
st.write(regression.summary())

# 根據預測結果預測下一天的價格
st.markdown("## Predicted AUO price for next day")
st.write(regression.predict(sm.add_constant(tsm_adr_close)))

# 預測結果與實際結果的差異

st.markdown("## Difference between predicted and actual AUO price")
