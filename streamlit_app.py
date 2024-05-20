import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Day': [1, 2, 3, 4, 5, 6, 7],
    'Germans': [2, 3, 5, 7, 8, 6, 7]
}

df = pd.DataFrame(data)

st.title('Number of Germans Living in Our Home Over Time')
st.subheader('Interactive Chart')

st.line_chart(df.set_index('Day'))

# Optional: Adding more interactive features
st.write('Data Table')
st.dataframe(df)

st.write('Statistics')
st.write(df.describe())
