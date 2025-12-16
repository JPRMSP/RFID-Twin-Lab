import streamlit as st
import math

st.set_page_config(page_title="RFID Twin Lab", layout="wide")

st.title("📡 RFID Twin Lab – Real-Time RFID System Simulator")
st.subheader("A Digital Twin for UHF RFID Performance Analysis")

st.sidebar.header("🔧 RFID Configuration")

frequency = st.sidebar.selectbox(
    "Operating Frequency (MHz)",
    [860, 915, 2450]
)

tx_power = st.sidebar.slider(
    "Reader Transmit Power (dBm)",
    20, 36, 30
)

antenna_gain = st.sidebar.slider(
    "Reader Antenna Gain (dBi)",
    0, 12, 6
)

polarization_loss = st.sidebar.selectbox(
    "Antenna Polarization",
    ["Matched", "Mismatched"]
)

sensor_enabled = st.sidebar.checkbox("Enable Sensor-Integrated RFID Tag")

st.divider()

c = 3e8
freq_hz = frequency * 1e6
wavelength = c / freq_hz

distance = st.slider(
    "Distance between Reader & Tag (meters)",
    0.5, 15.0, 5.0
)

path_loss = 20 * math.log10((4 * math.pi * distance) / wavelength)

pol_loss = 0 if polarization_loss == "Matched" else 3

received_power = tx_power + antenna_gain - path_loss - pol_loss

if sensor_enabled:
    received_power -= 2

st.header("📊 RFID System Performance")

col1, col2, col3 = st.columns(3)

col1.metric("Path Loss (dB)", f"{path_loss:.2f}")
col2.metric("Tag Received Power (dBm)", f"{received_power:.2f}")
col3.metric("Operating Wavelength (m)", f"{wavelength:.3f}")

st.divider()

st.header("🧠 Engineering Insights")

if received_power > -10:
    st.success("Excellent Tag Readability ✔️")
elif -20 < received_power <= -10:
    st.warning("Moderate Readability ⚠️")
else:
    st.error("Tag Detection Failed ❌")

st.markdown("""
### Key Observations
- Higher **antenna gain** increases read range
- **Polarization mismatch** reduces performance
- **Sensor-enabled tags** consume extra power
- Lower frequency improves penetration and range
""")

st.divider()

st.header("🌍 Real-Time Applications")
st.markdown("""
- Smart Warehousing  
- Contactless Access Control  
- Medical Equipment Tracking  
- Industrial Automation  
- Animal Identification  
""")

st.caption("Designed as per Anna University – FI9047 RFID Technology & Applications")
