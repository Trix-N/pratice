import streamlit as st



st.set_page_config(
    page_title="MAVIR Cross-border Flow",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state='collapsed',
    )



st.title('Counter Example')
count = 0

increment = st.button('Increment')
if increment:
    count += 1

st.write('Count = ', count)


