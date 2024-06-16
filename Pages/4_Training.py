import streamlit as st
import time
import numpy as np

st.set_page_config(page_title="Training Opportunities", page_icon="📚")

st.markdown("# Training Opportunities at Promket Oil and Gas Consult")
st.write(
    """ Promket Oil and Gas Consult offers training opportunities for students, graduates and professionals."""
)

training_opportunities = [
    "Basic crude oil and gas Production Operations",
    "Basic crude oil and gas drilling Operations",
    "Basic crude oil and gas reservoir Operations",
    "Oil field chemical applications",
    "Basic wellhead and production platform instrumentation",
    "Laboratory Safety & Safe Chemical Handling",
    "Basic introduction to statistics",
    "Advanced statistics and application",
    "Learning the fundamentals of Python",
    "Machine learning algorithms"
]

st.markdown("## Training Programs Available:")
for training in training_opportunities:
    st.write("- " + training)

