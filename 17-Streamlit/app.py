import streamlit as st
import pandas as pd
import numpy as np
import mymodel as m
st.title("This is big")
st.title("Hello streamlit")
st.write("Simple text")

df=pd.DataFrame({
    'first col':[1,2,3,4,5],
    'second col':[11,12,13,14,15]
})
st.write("Here is DF")
st.write(df)

chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.write(chart_data)
st.markdown(""""
            :rainbow[This is quite fun you don't have to do much more
            hehe this is a rainbow text]
            
                        
""")
st.line_chart(chart_data)
st.write(m.run(window=19))
st.button("send ballons")

