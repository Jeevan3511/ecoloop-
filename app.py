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

# ---------------------- KNOWLEDGE HUB TAB ----------------------
with tabs[5]:
    st.markdown("<h2 style='color:#4B0082;'>💡 Knowledge Hub</h2>", unsafe_allow_html=True)
    st.write("Learn from **real-world sustainability case studies** and get inspired by **powerful quotes**.")

    # Case Studies
    with st.expander("🌳 Afforestation in Andhra Pradesh"):
        st.write("""
        **Goal:** Increase green cover by 30% in 5 years.  
        **Impact:** 50,000+ trees planted, biodiversity restored.  
        **Lesson:** Community engagement is as important as planting trees.
        """)

    with st.expander("🌊 AI for Ocean Cleanup"):
        st.write("""
        **Goal:** Detect floating plastic and trigger cleanup drones.  
        **Impact:** 20 tons of waste removed in 6 months.  
        **Lesson:** Technology + activism accelerates change.
        """)

    with st.expander("☀️ Solar Villages in Rajasthan"):
        st.write("""
        **Goal:** Train rural women to install solar systems.  
        **Impact:** 1,300+ villages electrified, reducing fossil fuel use.  
        **Lesson:** Empowering locals creates lasting solutions.
        """)

    # Quotes
    st.markdown("### 🌟 Inspiring Quotes")
    quotes = [
        "“The best time to plant a tree was 20 years ago. The second best time is now.” – Chinese Proverb",
        "“We do not inherit the Earth from our ancestors, we borrow it from our children.” – Native American Proverb",
        "“Small acts, when multiplied by millions of people, can transform the world.” – Howard Zinn"
    ]
    for q in quotes:
        st.markdown(f"<div style='background-color:#f0f8ff; padding:10px; border-radius:8px;'>{q}</div>", unsafe_allow_html=True)

# ---------------------- FOOTER ----------------------
st.markdown("""
---
Made with ❤️ by JEEVAN MAGAPU | Promoting Sustainability | Inspired by the Five Elements 🌿
""")
