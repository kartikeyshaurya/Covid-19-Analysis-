import streamlit as st
from streamlit_embedcode import github_gist
import pandas as pd
import numpy as np

st.title("Covid 19 Data Analysis")

'''
#magic keywords 
st.write("Here's our first attempt at using data to create a table:")

df = pd.DataFrame({
'first column': [1, 2, 3, 4],
'second column': [10, 20, 30, 40]
})
df

'''

'''

# line chart 
chart_data = pd.DataFrame(
np.random.randn(20, 3),
columns=['a', 'b', 'c'])
st.line_chart(chart_data)
'''
# Plot 