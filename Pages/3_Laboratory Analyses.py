import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError

st.set_page_config(page_title="Promket Oil and Gas Consult", page_icon="🛢️")

st.markdown("# Promket Oil and Gas Consult")
st.sidebar.header("Physicochemical Analyses")
st.write(
    """This section showcases the physicochemical analyses carried out at Promket Oil and Gas Consult."""
)

# Dictionary of physicochemical analyses and their descriptions
analyses_data = {
    "Water Analysis": "Analysis of water samples to determine various parameters such as pH, conductivity, dissolved oxygen, etc.",
    "Soil Analysis": "Analysis of soil samples to assess properties like pH, organic carbon content, nutrient levels, etc.",
    "Oil Extraction": "Process of extracting oil from samples for further analysis and testing.",
    "Oil Characterization": "Detailed analysis of oil samples to determine composition and properties.",
    "Physical Appearance": "Visual examination of samples to assess their appearance, texture, etc.",
    "Colour": "Measurement and characterization of the color of samples.",
    "Odour": "Assessment of the odor characteristics of samples.",
    "pH": "Measurement of the acidity or alkalinity of samples.",
    "Specific Gravity": "Measurement of the density of samples relative to water.",
    "Electrical Conductivity": "Measurement of the ability of samples to conduct electricity.",
    "Dissolved Oxygen": "Measurement of the amount of oxygen dissolved in samples.",
    "Total Suspended Solids": "Measurement of the amount of suspended solids in liquid samples.",
    "Total Dissolved Solids": "Measurement of the amount of dissolved solids in liquid samples.",
    "Total Solids": "Measurement of the total amount of solids in samples.",
    "Chloride": "Measurement of the chloride ion concentration in samples.",
    "Salinity": "Measurement of the salt content in samples.",
    "Alkalinity": "Measurement of the alkaline properties of samples.",
    "Total Organic Carbon": "Measurement of the amount of carbon bound in organic compounds.",
    "Total Carbon": "Measurement of the total amount of carbon in samples.",
    "Ash Content": "Measurement of the mineral content left after complete combustion of samples.",
    "Ammonium Content": "Measurement of the ammonium ion concentration in samples.",
    "Phosphorus": "Measurement of the phosphorus content in samples.",
    "Phosphate": "Measurement of the phosphate ion concentration in samples.",
    "Nitrate": "Measurement of the nitrate ion concentration in samples.",
    "Nitrite": "Measurement of the nitrite ion concentration in samples.",
    "Sulphate": "Measurement of the sulfate ion concentration in samples.",
    "Sulphide": "Measurement of the sulfide ion concentration in samples.",
    "PAH (Polycyclic Aromatic Hydrocarbons)": "Analysis of PAH compounds in samples.",
    "TPH (Total Petroleum Hydrocarbons)": "Measurement of the total amount of petroleum hydrocarbons in samples.",
    "Heavy Metals": "Analysis of heavy metal concentrations in samples.",
    "Viscosity @40°C": "Measurement of the viscosity of samples at 40°C.",
    "Viscosity @60°C": "Measurement of the viscosity of samples at 60°C.",
    "Viscosity @100°C": "Measurement of the viscosity of samples at 100°C.",
    "Viscosity Index": "Measurement of the viscosity index of samples.",
    "Rheology": "Study of the flow properties of samples under different conditions.",
    "Pour Point": "Measurement of the temperature at which a sample begins to flow under specified conditions.",
    "Flash Point": "Measurement of the temperature at which a sample vaporizes and ignites in air."
}

# Display checkboxes for selecting analyses
selected_analyses = []
for analysis, description in analyses_data.items():
    if st.sidebar.checkbox(analysis, False):
        selected_analyses.append((analysis, description))

# Display selected analyses and their descriptions
if selected_analyses:
    st.markdown("## Selected Analyses")
    for analysis, description in selected_analyses:
        st.subheader(analysis)
        st.write(description)
else:
    st.error("Please select at least one physicochemical analysis.")

