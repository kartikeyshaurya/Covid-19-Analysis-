import streamlit as st
from streamlit_embedcode import github_gist
import pandas as pd
import numpy as np

st.title("Covid 19 Data Analysis")


#magic keywords 
st.write("Here's our first attempt at using data to create a table:")

df = pd.DataFrame({
'first column': [1, 2, 3, 4],
'second column': [10, 20, 30, 40]
})
df

chart_data = pd.DataFrame(
np.random.randn(20, 3),
columns=['a', 'b', 'c'])
st.line_chart(chart_data)  

map_data = pd.DataFrame(
np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
columns=['lat', 'lon'])
st.map(map_data)



github_gist("https://gist.github.com/wildjcrt/cda0ef5a729220225ac5bb1d6325e9e7")