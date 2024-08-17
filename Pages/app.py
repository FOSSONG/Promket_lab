import streamlit as st

# Import your pages
import About_Promket
import Laboratory_Equipment
import Laboratory_Analyses
import Training
import Consulting

# Set page configuration
st.set_page_config(
    page_title="PROMKET OIL AND GAS CONSULT NIGERIA LIMITED",
    page_icon= "F:\\PROMKET_STREAMLIT_PROJECT\\LOGO.png",
    layout="wide",  # Wide layout for better content arrangement
)

# Sidebar for navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Go to", ["Home", "About Promket", "Laboratory Equipment", "Laboratory Analyses", "Training", "Consulting"])

# Display the selected page
if options == "Home":
    st.title("Welcome to PROMKET OIL AND GAS CONSULT NIGERIA LIMITED 👋")
    st.write("Enjoy the ride!!.")
    st.image("F:\PROMKET_STREAMLIT_PROJECT\LOGO.png", caption="Promket consult Logo", use_column_width=False)
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
        - **Tel:** (+234)8027661375 / (+234)8039230721
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
elif options == "About Promket":
    About_Promket.show()
elif options == "Laboratory Equipment":
    Laboratory_Equipment.show()
elif options == "Laboratory Analyses":
    Laboratory_Analyses.show()
elif options == "Training":
    Training.show()
elif options == "Consulting":
    Consulting.show()

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
