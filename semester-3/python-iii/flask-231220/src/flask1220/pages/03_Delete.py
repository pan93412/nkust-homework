from typing import cast
import pandas as pd
from const import collection

import streamlit as st

items = list(collection.find())
st.dataframe(pd.DataFrame(items))

"## Delete what you want to delete"

delete_by = st.selectbox("刪除依據", map(str, items[0].keys()))
condition = st.text_input("刪除條件")


assert delete_by

# get the actual type of the value
typed_condition = type(items[0][delete_by])(condition)

try:
    result = None
    filter = {delete_by: typed_condition}

    st.write("Delete filter:", filter)

    if st.button("Delete one"):
        result = collection.delete_one(filter)
    elif st.button("Delete many"):
        result = collection.delete_many(filter)

    if result:
        st.write("Delete success (%d items)" % (result.deleted_count))
except Exception as e:
    st.write(e)
