import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="PROMKET Oil and Gas Consult",
    layout="centered",
)

def show():
    st.title("About PROMKET OIL AND GAS CONSULT NIGERIA LIMITED")
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

    st.write(
        """This demo showcases a summary of the processes that takes place in the oil and gas industry.
        # PROMKET OIL AND GAS CONSULT provides reliable services at every stage of the process.
        """
    )

    if st.button("click here"):
        st.video("https://youtu.be/RtURL0FW3KI?list=PL0gBJKv_mskxAz1I9BTa40aaotBq_CdNs")

    # DPR Permits Obtained section
    st.markdown("<div class='dpr-header'>DPR Permits Obtained</div>", unsafe_allow_html=True)
    st.markdown("1. Laboratory services - Chemical and mud testing")
    st.markdown("2. Onshore environmental/waste management - Environmental assessment/studies (EIA, EER, EAR, PIA)")
    st.markdown("3. Training")

# Call the show function to render the content
show()
