from typing import cast
import pandas as pd
from const import collection

import streamlit as st

items = list(collection.find())
st.dataframe(pd.DataFrame(items))

"## Update one"
filter_by = st.selectbox("Filter by", map(str, items[0].keys()))
filter_value = st.text_input("Filter value")
update_by = st.selectbox("Update by", map(str, items[0].keys()))
update_to = st.text_input("Update to")

assert update_by
assert filter_by

# get the actual type of the value
typed_update_to = type(items[0][update_by])(update_to)

result = None
filter = {filter_by: filter_value}
update = {"$set": {update_by: typed_update_to}}

st.write("Update filter:", filter)
st.write("Update:", update)

if st.button("Update"):
    result = collection.update_many(filter, update)

if result:
    st.write("Update success (%d items)" % (result.modified_count))
