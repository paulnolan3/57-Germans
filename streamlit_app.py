import streamlit as st
import pandas as pd

# Sample data with dates
data = {
    'Date': pd.date_range(start='2024-05-19', end='2024-05-26'),
    'Germans': [2, 3, 5, 7, 8, 6, 7, 5]
}

df = pd.DataFrame(data)

st.title('Number of Germans Living in Our Home Over Time')

st.line_chart(df.set_index('Date'))

# Optional: Adding more interactive features
st.write('Data Table')
st.dataframe(df)

st.write('Statistics')
st.write(df.describe())
