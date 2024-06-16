import streamlit as st
import time
import numpy as np

st.set_page_config(page_title="Promket Consulting", page_icon="🌟")

# Styling with CSS for a stylish header
st.markdown(
    """
    <style>
    .header {
        background-color: #f0f0f0;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .header-text {
        font-size: 24px;
        font-weight: bold;
        color: #333333;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header section
st.markdown("<div class='header'><p class='header-text'>Promket Consulting</p></div>", unsafe_allow_html=True)

# Consulting areas section
st.markdown("## Consulting Areas")

consulting_areas = [
    {"area": "Flow assurance", "description": "Ensuring efficient and uninterrupted flow of hydrocarbons from reservoir to market."},
    {"area": "Production operations", "description": "Optimizing oil and gas production processes to maximize efficiency and output."},
    {"area": "Drilling operations", "description": "Managing drilling activities to ensure safe and effective well construction."},
    {"area": "Petroleum reservoir operations", "description": "Strategizing reservoir management to maximize recovery and profitability."},
    {"area": "Environmental", "description": "Providing solutions for environmental impact assessments and management in oil and gas operations."}
]

for area in consulting_areas:
    st.write(f"### {area['area']}")
    st.write(area['description'])
    st.write("---")  # Divider between sections

# Plotting and animation demo
st.write(
    """
    ## Real-time Analyses Demo

    Do you wish to get real-time analyses and predictions for your operations? Do you wish to stay ahead 
    in this competitive oil and gas market? Look no further! we are here for you. Enjoy a demo!
    """
)

progress_bar = st.progress(0)
status_text = st.empty()
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)

for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text(f"{i}% Complete")
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.05)

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")
