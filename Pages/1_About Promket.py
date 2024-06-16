import streamlit as st
import numpy as np

st.set_page_config(page_title="PROMKET OIL AND GAS CONSULT, NIGERIA LIMITED", page_icon="🩸")

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main-header {
        font-size: 30px;
        color: #FFD700; /* Bright yellow color */
        font-family: 'Arial Black', Gadget, sans-serif;
        text-align: center;
    }
    .vision-header, .mission-header {
        font-size: 24px;
        color: #FF4500; /* Orange Red color */
        font-family: 'Verdana', Geneva, sans-serif;
        margin-top: 20px;
    }
    .vision, .mission {
        font-size: 20px;
        color: #ADD8E6; /* Light Blue color */
        font-family: 'Verdana', Geneva, sans-serif;
        margin-bottom: 20px;
    }
    .vision img, .mission img {
        display: block;
        margin-left: auto;
        margin-right: auto;
        margin-top: 10px;
        margin-bottom: 20px;
        border-radius: 10px;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    }
    .sidebar .sidebar-content {
        width: 250px;
    }
    .dpr-header {
        font-size: 24px;
        color: #008080; /* Teal color */
        font-family: 'Verdana', Geneva, sans-serif;
        margin-top: 20px;
    }
    .dpr-item {
        font-size: 18px;
        color: #008080; /* Teal color */
        font-family: 'Verdana', Geneva, sans-serif;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True
)

st.markdown("<div class='main-header'>PROMKET OIL AND GAS CONSULT, NIGERIA LIMITED</div>", unsafe_allow_html=True)

st.sidebar.header("About PROMKET")

st.markdown(
    """
    <div class="vision-header">Vision Statement</div>
    <div class="vision">
    To be a world-class Consultancy Company in Petrochemical and Environmental Management.
    <img src="https://static.vecteezy.com/system/resources/thumbnails/020/925/402/small_2x/vision-compass-close-up-photo.jpg" width="400">
    </div>
    """, unsafe_allow_html=True
)

st.markdown(
    """
    <div class="mission-header">Mission Statement</div>
    <div class="mission">
    To carry out world-class research for the advancement and development of local content in Nigeria, ensure high quality service, sound environmental management, and application of standard laboratory practice. The operations of the company would be at all times supported by professionally experienced and qualified engineers and technicians to ensure job safety to personnel and environment.
    <img src="https://www.giet.edu/wp-content/uploads/2020/11/mission.jpg" width="400">
    </div>
    """, unsafe_allow_html=True
)

st.write(
    """This demo showcases a summary of the processes that takes place in the oil and gas industry.
PROMKET OIL AND GAS CONSULT provides reliable services at every stage of the process.
"""
)

if st.button("Play Demo Video"):
    st.video("https://youtu.be/RtURL0FW3KI?list=PL0gBJKv_mskxAz1I9BTa40aaotBq_CdNs")

# DPR Permits Obtained section
st.markdown("<div class='dpr-header'>DPR Permits Obtained</div>", unsafe_allow_html=True)
st.markdown("1. Laboratory services - Chemical and mud testing")
st.markdown("2. Onshore environmental/waste management - Environmental assessment/studies (EIA, EER, EAR, PIA)")
st.markdown("3. Training")
