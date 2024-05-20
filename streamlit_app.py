import streamlit as st
import pandas as pd
import altair as alt

# Sample data with dates and two series
data = {
    'Date': pd.date_range(start='2024-05-19', end='2024-05-26'),
    'Actual_Germans': [2, 3, 5, 7, 8, 6, 7, 5],
    'Anticipated_Germans': [2, 4, 6, 7, 9, 8, 7, 6]
}

df = pd.DataFrame(data)

st.title('Number of Germans Living in Our Home Over Time')

# Define the Altair chart
chart = alt.Chart(df).transform_fold(
    ['Actual_Germans', 'Anticipated_Germans'],
    as_=['Legend', 'Number of Germans']
).mark_line().encode(
    x='Date:T',
    y='Number of Germans:Q',
    color=alt.condition(
        alt.datum.Legend == 'Actual_Germans',
        alt.value('blue'),  # Actual series color
        alt.value('lightgray')  # Anticipated series color
    ),
    strokeDash=alt.condition(
        alt.datum.Legend == 'Anticipated_Germans',
        alt.value([5, 5]),  # Dashed line for anticipated series
        alt.value([0])  # Solid line for actual series
    ),
    tooltip=['Date:T', 'Legend:N', 'Number of Germans:Q']
).properties(
    width=600,
    height=400
).interactive()

st.altair_chart(chart, use_container_width=True)

# Optional: Adding customized statistics
st.write('Statistics')
custom_stats = df.describe().drop(['25%', '50%', '75%'])
st.write(custom_stats)
