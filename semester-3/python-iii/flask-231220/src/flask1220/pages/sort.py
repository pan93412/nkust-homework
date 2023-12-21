from typing import cast
import pandas as pd
from const import collection

import streamlit as st

item = collection.find()[0]

"## sort the result"

sort_by = st.selectbox("Sort by", list(filter(lambda v: v != "_id", cast(list[str], item.keys()))))
sort_order = st.selectbox("Sort order", ["asc", "desc"])

assert sort_by is not None

try:
    data = pd.DataFrame(collection.find({}).sort(sort_by, 1 if sort_order == "asc" else -1))
    data.set_index("_id", inplace=True)
    st.dataframe(data)
except KeyError:
    st.write("No results.")
except Exception as e:
    st.write(e)
