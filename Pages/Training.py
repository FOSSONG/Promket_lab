import streamlit as st
import time
import numpy as np

def show():
    st.title("Training")

    st.markdown("# Training Opportunities at Promket Oil and Gas Consult")
    st.write(
        """Promket Oil and Gas Consult offers training opportunities for students, graduates, and professionals."""
    )

    training_opportunities = [
        "Basic and advance crude oil and gas Production Operations",
        "Basic and advance crude oil and gas drilling Operations",
        "Basic and advance crude oil and gas reservoir Operations",
        "Oil field chemical applications",
        "Basic and advance wellhead and production platform instrumentation",
        "Industrial Safety", 
        "Office Safety", 
        "General safety",
        "Basic introduction to statistics",
        "Advanced statistics and application",
        "Learning the fundamentals of Python",
        "Machine learning algorithms"
    ]

    st.markdown("## Training Programs Available:")
    for training in training_opportunities:
        st.write("- " + training)
