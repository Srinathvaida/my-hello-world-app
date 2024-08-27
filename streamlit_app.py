import streamlit as st
import numpy as np
import pandas as pd
st.title("Hello World!")
st.header("This is a header with a divider", divider="rainbow")
st.markdown("*Streamlit* is **really** ***cool***.")
col1,col2 = st.columns(2)
with col1:
    st.header("st.column")
    x = st.slider("mark the x value:",0,10)
with col2:
    
    st.write("the value of :red[***x***] is",x)
st.header("st.area_chart")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.area_chart(chart_data)
