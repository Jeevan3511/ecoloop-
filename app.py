import streamlit as st
from datetime import datetime

st.set_page_config(page_title="EcoLoop+ | AI for Sustainability", layout="wide")

# ---------------------- HEADER ----------------------
st.title("🌍 EcoLoop+ – Sustainability App")
st.markdown("""
Welcome to **EcoLoop+**, a sustainability dashboard combining afforestation modeling,
marine waste detection, energy tracking, commuting impact, and digital waste analysis through the lens of the **Pancha Bhootas** – Earth, Water, Fire, Air, and Space.
""")

# ---------------------- TABS ----------------------
tabs = st.tabs(["Earth 🌱", "Water 🌊", "Fire 🔥", "Air 🌬️", "Space 🌌", "Knowledge Hub 📚"])

# ---------------------- EARTH TAB ----------------------
with tabs[0]:
    st.header("Afforestation & CO₂ Sequestration")
    tree_species = st.selectbox("Choose Tree Species:", ["Banyan", "Neem", "Indian Almond", "Peepal"])
    age = st.slider("Tree Age (in years):", 1, 100, 10)

    species_factors = {"Banyan": 22, "Neem": 18, "Indian Almond": 20, "Peepal": 25}
    sequestration = species_factors[tree_species] * (age ** 1.2)
    st.success(f"Estimated CO₂ Sequestration: **{sequestration:.2f} kg/year**")

# ---------------------- WATER TAB ----------------------
with tabs[1]:
    st.header("Marine Plastic Waste Detection")
    uploaded = st.file_uploader("Upload a water body image to detect plastic waste:", type=["jpg", "png"])
    if uploaded:
        st.image(uploaded, caption="Uploaded Image", use_column_width=True)
        st.info("Using AI to detect pollution levels (demo)")
        st.success("Result: High pollution level detected – Bottles, Bags visible")
    else:
        st.markdown("⚠️ Upload an image of a river, lake or beach to assess pollution levels.")

# ---------------------- FIRE TAB ----------------------
with tabs[2]:
    st.header("Energy & Digital Footprint")
    screen_time = st.slider("Average daily screen time (in hours):", 1, 15, 6)
    device_count = st.number_input("Number of devices you use daily:", min_value=1, max_value=10, value=3)
    energy_consumed = screen_time * device_count * 0.12
    st.metric(label="Estimated Daily Energy Use", value=f"{energy_consumed:.2f} kWh")

    ai_model_usage = st.slider("Monthly AI model usage (hours):", 0, 100, 10)
    ai_emissions = ai_model_usage * 20
    st.metric("AI Carbon Footprint Estimate", f"{ai_emissions:.2f} kg/month")

    if ai_emissions > 100:
        st.warning("⚠️ High AI usage detected. Optimize your AI workflows to reduce emissions.")

# ---------------------- AIR TAB ----------------------
with tabs[3]:
    st.header("Commuting & Carbon Emissions")
    mode = st.selectbox("Your primary travel mode:", ["Cycle", "Walk", "Bus", "Petrol Bike", "Electric Scooter"])
    distance = st.slider("Daily commute distance (km):", 1, 100, 10)
    emission_factors = {"Cycle": 0, "Walk": 0, "Bus": 0.05, "Petrol Bike": 0.12, "Electric Scooter": 0.02}
    emissions = emission_factors[mode] * distance
    st.metric("Daily CO₂ Emissions from Travel", f"{emissions:.2f} kg")
    if emissions > 1:
        st.info("Try shifting to greener modes like walking or biking for short distances.")

# ---------------------- SPACE TAB ----------------------
with tabs[4]:
    st.header("E-Waste & Digital Sustainability")
    gadgets = st.multiselect("Select the gadgets you discard frequently:", ["Phone", "Charger", "Earphones", "Laptop", "Smartwatch"])
    st.write(f"You selected {len(gadgets)} items. Recycle or donate to reduce digital waste.")
    st.info("💡 Tip: Store unused electronics in a designated e-waste box.")
# ---------------------- KNOWLEDGE HUB (Simplified Colorful Cards) ----------------------
with tabs[5]:
    st.header("📚 Knowledge Hub — Learn · Get Inspired · Act")

    st.markdown("""
    <style>
    .kh-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 15px; }
    .kh-card {
        border-radius: 12px;
        padding: 14px;
        color: #222;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        font-family: "Segoe UI", sans-serif;
    }
    .earth  { background: #e6f4ea; border-left: 6px solid #2e7d32; }
    .water  { background: #e0f7fa; border-left: 6px solid #0288d1; }
    .energy { background: #fff3e0; border-left: 6px solid #f57c00; }
    .air    { background: #f1f8ff; border-left: 6px solid #00acc1; }
    .quote  { background: #f3e5f5; border-left: 6px solid #6a1b9a; }
    .kh-title { font-weight: 700; font-size: 18px; margin-bottom: 6px; }
    .kh-text { font-size: 14px; line-height: 1.4; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='kh-grid'>", unsafe_allow_html=True)

    st.markdown("""
    <div class='kh-card earth'>
      <div class='kh-title'>🌱 Urban Tree Planting</div>
      <div class='kh-text'>A city program in Hyderabad planted 1 million native trees in 3 years, cooling urban areas and improving air quality.</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='kh-card water'>
      <div class='kh-title'>💧 Rainwater Harvesting</div>
      <div class='kh-text'>A Chennai school installed rainwater tanks, saving 30% of its annual water use and reducing flooding.</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='kh-card energy'>
      <div class='kh-title'>⚡ Solar Rooftop Success</div>
      <div class='kh-text'>A rural community center in Maharashtra switched to solar, cutting energy bills by 70%.</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='kh-card air'>
      <div class='kh-title'>🚲 Cycling Initiative</div>
      <div class='kh-text'>Pune’s bike-sharing program reduced short car trips by 25%, lowering air pollution levels in key districts.</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='kh-card quote'>
      <div class='kh-title'>💬 Quote</div>
      <div class='kh-text'><i>“We do not inherit the Earth from our ancestors; we borrow it from our children.”</i></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
# ---------------------- FOOTER ----------------------
st.markdown("""
---
Made with ❤️ by JEEVAN MAGAPU | Promoting Sustainability | Inspired by the Five Elements 🌿
""")
