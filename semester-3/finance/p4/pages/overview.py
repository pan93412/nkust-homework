import streamlit as st
from base import close, returns

st.write("# 收盤價")
st.write(close)

#---
st.write("# 單期簡單收益率")
st.write(returns)

#---
st.write("# 相關係數矩陣")
st.write(returns.corr())
