from typing import cast
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

try:
    data = pd.DataFrame(collection.find({"age": {mode: ages}}))
    data.set_index("_id", inplace=True)
    st.dataframe(data)
except KeyError:
    st.write("No results.")
except Exception as e:
    st.write(e)

"## and & or with customized operators"

mode = st.selectbox("模式", ["$and", "$or"])
fields = st.multiselect("欄位", cast(list[str], items[0].keys()))

queries_inside_fields = []
for field in fields:
    with st.expander(field):
        is_ne = st.toggle("ne?", key=field+"__ne")
        value = st.text_input("value", key=field+"__value")
        queries_inside_fields.append({field: value if not is_ne else {"$ne": value}})

full_query = {mode: queries_inside_fields}
st.write("Query:", full_query)
try:
    data = pd.DataFrame(collection.find(full_query))
    data.set_index("_id", inplace=True)
    st.dataframe(data)
except KeyError:
    st.write("No results.")
except Exception as e:
    st.write("Query failed due to", e)
