import pandas as pd
from const import collection

import streamlit as st

items = collection.find()
items = list(items)

with st.expander("All items"):
    st.dataframe(items)

"## in 和 not in – 以 age 為例"

mode = st.selectbox("模式", ["$in", "$nin"])
ages = st.multiselect("age", list(set([item["age"] for item in items])))

data = pd.DataFrame(collection.find({"age": {mode: ages}}))
data.set_index("_id", inplace=True)
st.dataframe(data)
