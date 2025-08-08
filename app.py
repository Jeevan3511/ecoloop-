import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import base64

st.set_page_config(page_title="EcoLoop+ | AI for Sustainability", layout="wide")

# ---------------------- HEADER ----------------------
st.title("🌍 EcoLoop+ – AI-Powered Sustainability App")
st.markdown("""
Welcome to **EcoLoop+**, an AI-enhanced sustainability dashboard combining afforestation modeling,
marine waste detection, energy tracking, commuting impact, and digital waste analysis through the lens of the **Pancha Bhootas** – Earth, Water, Fire, Air, and Space.
""")

# ---------------------- TABS ----------------------
tabs = st.tabs(["Earth 🌱", "Water 🌊", "Fire 🔥", "Air 🌬️", "Space 🌌", "Eco AI Insights 🧠"])

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
    st.header("Marine Plastic Waste Detection (AI)")
    uploaded = st.file_uploader("Upload a water body image to detect plastic waste:", type=["jpg", "png"])
    if uploaded:
        st.image(uploaded, caption="Uploaded Image", use_column_width=True)
        st.info("Using AI to detect pollution levels (placeholder)")
        st.success("Result: High pollution level detected – Bottles, Bags visible")
    else:
        st.markdown("⚠️ Upload an image of a river, lake or beach to assess pollution levels using AI.")

# ---------------------- FIRE TAB ----------------------
with tabs[2]:
    st.header("Energy & Digital Footprint")
    screen_time = st.slider("Average daily screen time (in hours):", 1, 15, 6)
    device_count = st.number_input("Number of devices you use daily:", min_value=1, max_value=10, value=3)
    energy_consumed = screen_time * device_count * 0.12  # updated to 0.12 kWh/hour
    st.metric(label="Estimated Daily Energy Use", value=f"{energy_consumed:.2f} kWh")

    ai_model_usage = st.slider("Monthly AI model usage (hours):", 0, 100, 10)
    ai_emissions = ai_model_usage * 20  # 20 kg CO2 per GPU hour
    st.metric("AI Carbon Footprint Estimate", f"{ai_emissions:.2f} kg/month")

    if ai_emissions > 100:
        st.warning("⚠️ High AI usage detected. Consider optimizing your AI workflows to reduce emissions.")

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

# ---------------------- AI INSIGHTS TAB ----------------------
with tabs[5]:
    st.header("Eco AI Insights (Beta)")
    st.markdown("AI-generated sustainability summary based on your inputs")

    eco_score = 100 - (emissions + energy_consumed + ai_emissions * 0.2 + len(gadgets) * 3)
    eco_score = max(0, min(eco_score, 100))
    
    st.subheader(f"♻️ Eco Sustainability Score: {eco_score:.1f}/100")
    if eco_score > 85:
        st.success("🌟 Excellent! You're an Eco Champion.")
    elif eco_score > 60:
        st.info("👍 Good work. Small steps lead to big changes.")
    else:
        st.warning("🔧 Room for improvement. Try reducing device and energy usage.")

# ---------------------- FOOTER ----------------------
st.markdown("""
---
Made with ❤️ by JEEVAN MAGAPU | Promoting Sustainability with AI | Inspired by the Five Elements 🌿
""")
