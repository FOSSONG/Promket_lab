import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="PROMKET OIL AND GAS CONSULT NIGERIA LIMITED",
    page_icon="👋",
    layout="wide",  # Wide layout for better content arrangement
)

# Header with welcome message and emoji
st.title("Welcome to PROMKET OIL AND GAS CONSULT NIGERIA LIMITED 👋")

# Sidebar with a success message
st.sidebar.success("Please select a page above to view our catalogue.")

# Main content area with information
st.markdown(
    """
    ### About Us

    **PROMKET Oil and Gas Consult Nigeria Limited** is dedicated to providing top-notch consultancy services 
    in the oil and gas industry. Our services include:

    - Flow assurance
    - Production operations
    - Drilling operations
    - Petroleum reservoir operations
    - Environmental assessments
    
    We pride ourselves on delivering excellence and advancing local content in Nigeria.

    ---
    
    ### Contact Information
    
    - **Email:** promketconsultltd@gmail.com
    - **Tel:** 08039230721
    - **Address:** #72A Aliaparanwo Road, ObioAkpor L.G.A. Rivers State, Nigeria.

    ---
    
    ### Services Offered
    
    - Laboratory services - Chemical and mud testing
    - Onshore environmental/waste management - Environmental assessment/studies (EIA, EER, EAR, PIA)
    - Training opportunities
    
    ---
    
    ### DPR Permits Obtained
    
    1. Laboratory services - Chemical and mud testing
    2. Onshore environmental/waste management - Environmental assessment/studies (EIA, EER, EAR, PIA)
    3. Training
    """
)

# Add a footer or closing remark
st.markdown("---")
st.markdown("Thank you for visiting us! For more information, please explore the options above.")

# Optionally, you can add some CSS to style certain elements further
st.markdown(
    """
    <style>
    body {
        background-color: #f0f0f5;  /* Light grey background */
        font-family: Arial, sans-serif;
        line-height: 1.6;
    }
    .sidebar .sidebar-content {
        background-color: #ffffff;  /* White sidebar */
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.1);  /* Soft shadow */
    }
    .markdown-text {
        padding: 20px;
        background-color: #ffffff;  /* White content area */
        border-radius: 10px;
        box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.1);  /* Soft shadow */
    }
    </style>
    """,
    unsafe_allow_html=True
)
