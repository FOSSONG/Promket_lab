import streamlit as st

def show():
    st.title("Laboratory Equipment")

    st.markdown("# PROMKET Petrochemical and Environmental Laboratory")
    st.sidebar.header("Available Equipment in the Laboratory")
    st.write(
        """This section shows the various equipment available in PROMIKET Petrochemical and Environmental Laboratory. Select an equipment to view its details."""
    )

    equipment_data = {
        "Pour Point Determination equipment": {
            "description": "Pour point determination equipment can be used to determine the pour point of waxy crude oil.",
            "image": "https://raw.githubusercontent.com/FOSSONG/Promket_lab/main/POUR%20POINT%20DETERMINATION%20EQUIPMENT.png"
        },
        "Differential Scanning Calorimeter 800": {
            "description": "Differential scanning calorimeter (DSC 800) can be used to determine cold crystallization, phase transition, melting, crystallization, product stability, curing reaction temperature, and thermal effect measurement.",
            "image": "https://raw.githubusercontent.com/FOSSONG/Promket_lab/main/DIFFERENTIAL%20SCANNING%20CALORIMETER%20800.png"
        },
        "Atomic Absorption Spectrometer (AA320N)": {
            "description": "Atomic Absorption Spectrometer (AA320N) can be used to determine heavy metals in water samples, including Sodium (Na), Magnesium (Mg), Calcium (Ca), Iron (Fe), Lead (Pb), Chromium (Cr), Barium (Ba), Mercury (Hg), and Copper (Cu).",
            "image": "https://raw.githubusercontent.com/FOSSONG/Promket_lab/main/ATOMIC%20ABSORPTION%20SPECTROMETER%20(AA320N).png"
        },
        "Gas Chromatography (GC-7890)": {
            "description": "Gas chromatography (GC-7890) can be used to determine Speciated Total Petroleum Hydrocarbon (STPH) C8-C40 and Total Petroleum Hydrocarbon (TPH) - Paraffinic crude oil wax content.",
            "image": "https://raw.githubusercontent.com/FOSSONG/Promket_lab/main/GAS%20CHROMATOGRAPHY%20(GC%20-%207890).png"
        },
        "Twelve Speed Rotary Viscometer": {
            "description": "Twelve speed rotary viscometer can be used to test the rheology of petroleum, chemical, medicine, cosmetics, and other industry and research liquids.",
            "image": "https://raw.githubusercontent.com/FOSSONG/Promket_lab/main/TWELVE%20(12)%20SPEED%20ROTARY%20VISCOMETER.png"
        },
        "NDJ-8S Digital Rotary Viscometer": {
            "description": "NDJ-8S Digital rotary viscometer can be used to determine and measure liquid viscosity in many applications such as grease, paint, pharmacy, and adhesive.",
            "image": "https://raw.githubusercontent.com/FOSSONG/Promket_lab/main/NDJ%20-%208S%20DIGITAL%20ROTARY%20VISCOMETER.png"
        },
        "Flash Point and Ignition Point Analyser": {
            "description": "The flash point analyser can be used to determine the ignition temperature of volatile substances.",
            "image": "https://raw.githubusercontent.com/FOSSONG/Promket_lab/main/FLASH%20POINT%20AND%20IGNITION%20POINT%20ANALYSER.png"
        },   
        "Hamilton Beach Mixer": {
            "description": "Hamilton beach mixer can be used to mix mud samples with additives at given designed proportion to ascertain its effect on the rheological properties of drilling mud.",
            "image": "https://raw.githubusercontent.com/FOSSONG/Promket_lab/main/HAMILTON%20BEACH%20MIXER.png"
        },
        "ThermoCup": {
            "description": "The ThermoCup can be used to determine the effect of varying temperature on the rheological property of drilling mud or hydrocarbon.",
            "image": "https://raw.githubusercontent.com/FOSSONG/Promket_lab/main/THERMO%20CUP.png"
        },
        "Centrifuge Machine": {
            "description": "Centrifuge machine is used to separate substances based on their differential densities. It can be used to determine the Base Sediment and Water (BS&W) of crude oil.",
            "image": "https://raw.githubusercontent.com/FOSSONG/Promket_lab/main/CENTRIFUGE%20MACHINE.png"
        },
        "Magnetic Stirrer": {
            "description": "Magnetic stirrer can be used to mix solvents or reagents to form a homogeneous solution.",
            "image": "https://raw.githubusercontent.com/FOSSONG/Promket_lab/main/MAGNETIC%20STIRRER.png"
        },
        "pH Meter": {
            "description": "The pH meter is used to determine the pH of liquids.",
            "image": "https://raw.githubusercontent.com/FOSSONG/Promket_lab/main/pH%20METER.png"
        },
        "Fume Cupboard": {
            "description": "Fume cupboard is used for sample preparation to prevent inhaling toxic fumes or gases, which are removed with the aid of an air expeller.",
            "image": "https://raw.githubusercontent.com/FOSSONG/Promket_lab/main/FUME%20CUPBOARD.png"
        },
        "Wet Chemistry Concrete Table and Apparatus": {
            "description": "The wet chemistry concrete table and apparatus are used to conduct wet chemistry chemical analysis.",
            "image": "https://raw.githubusercontent.com/FOSSONG/Promket_lab/main/WET%20CHEMISTRY%20CONCRETE%20TABLE%20AND%20APPARATUS.png"
        },
    }

    selected_equipment = st.sidebar.selectbox("Select Equipment", list(equipment_data.keys()), index=0)

    if selected_equipment:
        st.markdown(f"## {selected_equipment}")
        try:
            st.image(equipment_data[selected_equipment]["image"], caption=selected_equipment, width=400)
        except Exception as e:
            st.error(f"Failed to load image: {e}")
        st.write(equipment_data[selected_equipment]["description"])
