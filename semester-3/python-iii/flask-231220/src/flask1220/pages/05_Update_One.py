from typing import cast
import pandas as pd
from const import collection

import streamlit as st

items = list(collection.find())
st.dataframe(pd.DataFrame(items))

"## Update one"
serial = st.number_input("What to update?", min_value=1, max_value=len(items), value=1)
update_by = st.selectbox("Update by", map(str, items[0].keys()))
assert update_by

update_to = st.text_input("Update to", value=items[int(serial)][update_by])

# get the actual type of the value
typed_update_to = type(items[0][update_by])(update_to)

result = None
filter = {"_id": items[int(serial)]["_id"]}
update = {"$set": {update_by: typed_update_to}}

st.write("Update filter:", filter)
st.write("Update:", update)

if st.button("Update"):
    result = collection.update_one(filter, update)

if result:
    st.write("Update success (%d items)" % (result.modified_count))
