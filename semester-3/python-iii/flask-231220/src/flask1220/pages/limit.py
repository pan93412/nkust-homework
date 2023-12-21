from typing import cast
import pandas as pd
from const import collection

import streamlit as st

"## limit"

limit = st.number_input("Limit", min_value=1, max_value=100, value=1)

try:
    data = pd.DataFrame(collection.find({}).limit(int(limit)))
    data.set_index("_id", inplace=True)
    st.dataframe(data)
except KeyError:
    st.write("No results.")
except Exception as e:
    st.write(e)
