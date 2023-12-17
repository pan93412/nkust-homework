import pandas as pd
from pypfopt import expected_returns, EfficientSemivariance
import streamlit as st
from base import returns, close

st.write("# 馬可維茲投資組合資產配置")

st.write("我們選擇 2014-2015 年資料進行模型建立。")
train_set = close['2014-01-01':'2015-12-31']
test_set = close['2016-01-01':]

st.write("## 訓練集")
st.write(train_set)

st.write("## 測試集")
st.write(test_set)

st.write("求共變異數矩陣。")
mu = expected_returns.mean_historical_return(train_set)
historical_returns = expected_returns.returns_from_prices(train_set)
st.write(mu)
st.write(historical_returns)

st.write("限制只能做多，不能做空。目標收益率 0.6%")
es = EfficientSemivariance(mu, historical_returns)
es.efficient_return(0.0006)

weights = es.clean_weights()
st.write(weights)

st.write("## 進行資產配置並計算累積收益率")
test_return = expected_returns.returns_from_prices(test_set).dot(pd.Series(weights))
test_cum_return = (1 + test_return).cumprod() - 1
st.write(test_cum_return)
st.line_chart(test_cum_return)
