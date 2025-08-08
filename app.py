import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

st.set_page_config(page_title="EcoLoop+ | AI for Sustainability", layout="wide")

# ---------------------- HEADER ----------------------
st.title("🌍 EcoLoop+ – AI-Powered Sustainability App")
st.markdown("""
Welcome to **EcoLoop+**, an AI-enhanced sustainability dashboard combining afforestation modeling,
marine waste awareness, and eco-habit tracking based on the **Pancha Bhootas** – Earth, Water, Fire, Air, and Space.
""")

# ---------------------- TABS ----------------------
tabs = st.tabs(["Earth 🌱", "Water 🌊", "Fire 🔥", "Air 🌬️", "Space 🌌", "Eco AI Insights 🧠"])

# ---------------------- EARTH TAB ----------------------
with tabs[0]:
    st.header("Afforestation & CO₂ Sequestration")
    tree_species = st.selectbox("Choose Tree Species:", ["Banyan", "Neem", "Indian Almond", "Peepal"])
    age = st.slider("Tree Age (in years):", 1, 100, 10)

    # Simple model: sequestration = species_factor * age ^ 1.2
    species_factors = {"Banyan": 22, "Neem": 18, "Indian Almond": 20, "Peepal": 25}
    sequestration = species_factors[tree_species] * (age ** 1.2)
    st.success(f"Estimated CO₂ Sequestration: **{sequestration:.2f} kg/year**")

# ---------------------- WATER TAB ----------------------
with tabs[1]:
    st.header("Marine Plastic Waste Awareness")
    uploaded = st.file_uploader("Upload a beach or water body image to detect plastic waste:", type=["jpg", "png"])
    if uploaded:
        st.image(uploaded, caption="Uploaded Image", use_column_width=True)
        st.info("(AI detection placeholder) Plastic items detected: Bottles, Bags, Straws")
        st.success("Awareness Level: High – Consider joining a local cleanup drive!")

# ---------------------- FIRE TAB ----------------------
with tabs[2]:
    st.header("Energy & Digital Footprint")
    screen_time = st.slider("Average daily screen time (in hours):", 1, 15, 6)
    device_count = st.number_input("Number of devices you use daily:", min_value=1, max_value=10, value=3)
    energy_consumed = screen_time * device_count * 0.1  # kWh
    st.metric(label="Estimated Daily Energy Use", value=f"{energy_consumed:.2f} kWh")
    if energy_consumed > 3:
        st.warning("High usage – Try reducing screen time or using power-saving modes.")

# ---------------------- AIR TAB ----------------------
with tabs[3]:
    st.header("Commuting & Carbon Emissions")
    mode = st.selectbox("Your primary travel mode:", ["Cycle", "Walk", "Bus", "Petrol Bike", "Electric Scooter"])
    distance = st.slider("Daily commute distance (km):", 1, 100, 10)
    emission_factors = {"Cycle": 0, "Walk": 0, "Bus": 0.05, "Petrol Bike": 0.12, "Electric Scooter": 0.02}
    emissions = emission_factors[mode] * distance
    st.metric("Daily CO₂ Emissions from Travel", f"{emissions:.2f} kg")
    if emissions > 1:
        st.info("Try shifting to sustainable travel for shorter distances!")

# ---------------------- SPACE TAB ----------------------
with tabs[4]:
    st.header("E-Waste & Sustainable Tech Habits")
    gadgets = st.multiselect("Select the gadgets you discard frequently:", ["Phone", "Charger", "Earphones", "Laptop", "Smartwatch"])
    st.write(f"You selected {len(gadgets)} items. Consider recycling or donating usable tech!")
    st.info("Try storing unused electronics in a designated e-waste box.")

# ---------------------- AI INSIGHTS TAB ----------------------
with tabs[5]:
    st.header("Eco AI Insights (Beta)")
    st.markdown("Generating AI-based recommendations from your activity...")
    eco_score = 100 - (emissions + energy_consumed + len(gadgets) * 2)
    eco_score = max(0, min(eco_score, 100))

    st.subheader(f"🧭 Your Eco Sustainability Score: {eco_score:.1f}/100")
    if eco_score > 80:
        st.success("Excellent! You're an Eco Champion! 🌟")
    elif eco_score > 50:
        st.info("Good progress. Keep improving your habits.")
    else:
        st.warning("You can do better! Start small – every action counts.")

# ---------------------- FOOTER ----------------------
st.markdown("""
---
Made with ❤️ for a better planet. 
**EcoLoop+** blends afforestation, marine protection, and tech-conscious living to support the **SDGs**.
""")
