import streamlit as st
import pandas as pd

# Sample data with dates and two series
data = {
    'Date': pd.date_range(start='2024-05-19', end='2024-05-26'),
    'Actual_Germans': [2, 3, 5, 7, 8, 6, 7, 5],
    'Anticipated_Germans': [2, 4, 6, 7, 9, 8, 7, 6]
}

df = pd.DataFrame(data)

st.title('Number of Germans Living in Our Home Over Time')

# Creating the chart
st.line_chart(df.set_index('Date')[['Actual_Germans', 'Anticipated_Germans']], width=600, height=400)

# Optional: Adding customized statistics
st.write('Statistics')
custom_stats = df.describe().drop(['25%', '50%', '75%'])
st.write(custom_stats)
