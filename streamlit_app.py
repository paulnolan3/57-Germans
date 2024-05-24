import streamlit as st
import pandas as pd
import altair as alt

# Sample data with dates and two series
data = {
    'Date': pd.date_range(start='2024-05-18', end='2024-05-26'),
    'Actual_Germans': [2, 3, 5, 13, 13, 13, 8, None, None],
    'Anticipated_Germans': [2, 3, 6, 11, 12, 12, 9, 7, 5]
}

df = pd.DataFrame(data).set_index('Date')

st.title('Count of Germans at 57 Aldie')

# Create the base chart
base = alt.Chart(df.reset_index()).encode(
    x='Date:T',
    y=alt.Y('value:Q', title='Number of Germans')
).transform_fold(
    ['Actual_Germans', 'Anticipated_Germans'],
    as_=['Legend', 'value']
)

# Line for actual and anticipated Germans
line = base.mark_line().encode(
    color=alt.Color('Legend:N', scale=alt.Scale(range=['blue', 'gray']), legend=None),
    strokeDash=alt.condition(
        alt.datum.Legend == 'Anticipated_Germans',
        alt.value([5, 5]),  # Dashed line for anticipated series
        alt.value([0])  # Solid line for actual series
    )
)

# Points for actual Germans with flag emoji
points = alt.Chart(df.reset_index()).mark_text(
    align='left',
    baseline='middle',
    dx=7,  # Adjust the position of the emoji
    fontSize=16
).encode(
    x='Date:T',
    y='Actual_Germans:Q',
    text=alt.value('🇩🇪')
)

# Combine the line and points
chart = (line + points).properties(
    width=600,
    height=400
).interactive()

st.altair_chart(chart, use_container_width=True)

# Optional: Adding customized statistics
st.write('German Statistics')
custom_stats = df.describe().drop(['25%', '50%', '75%'])
st.write(custom_stats)
