from typing import cast
import pandas as pd
from const import collection

import streamlit as st

items = list(collection.find())
st.dataframe(pd.DataFrame(items))

"## Drop Table"

if st.button("Drop"):
    collection.drop()
    st.write("Drop success.")
