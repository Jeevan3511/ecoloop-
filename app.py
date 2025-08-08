# ecoloop_app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

st.set_page_config(page_title="EcoLoop+ – AI for Sustainable Circles of Life", layout="wide")

st.title("🌍 EcoLoop+ – AI for Sustainable Circles of Life")
st.markdown("Track your daily actions and see how they affect Earth 🌱, Water 🌊, Fire 🔥, Air 💨, and Space 🌌.")

# --- Form ---
with st.form("eco_form"):
    st.header("📋 Daily Sustainability Tracker")
    
    col1, col2 = st.columns(2)
    
    with col1:
        waste = st.slider("Plastic Waste (grams)", 0, 500, 50)
        transport = st.selectbox("Mode of Transport Today", ["Walking", "Cycling", "Bus", "Car", "Bike"])
        electricity = st.slider("Electricity Used (kWh)", 0, 20, 5)
    
    with col2:
        screen_time = st.slider("Screen Time (hrs)", 0, 15, 5)
        water_used = st.slider("Water Used (litres)", 0, 500, 100)
        tree_planted = st.number_input("No. of Trees Planted Today", min_value=0, step=1)

    submitted = st.form_submit_button("🔍 Analyze My Eco Impact")

# --- Analysis ---
if submitted:
    # Simple AI scoring logic (can be improved)
    scores = {
        "Earth": max(0, 10 - waste / 50 + tree_planted),
        "Water": max(0, 10 - water_used / 50),
        "Fire": max(0, 10 - electricity / 2),
        "Air": 10 if transport in ["Walking", "Cycling"] else 5 if transport == "Bus" else 3,
        "Space": max(0, 10 - screen_time)
    }

    df = pd.DataFrame(scores, index=["Score"]).T
    st.subheader("🌀 Elemental Balance (AI Score)")
    st.dataframe(df)

    # --- Radar Chart ---
    categories = list(scores.keys())
    values = list(scores.values())
    values += values[:1]  # repeat first for closed loop

    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.plot(angles, values, linewidth=2)
    ax.fill(angles, values, alpha=0.25)
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    st.pyplot(fig)

    # --- Save Entry ---
    entry = {
        "Date": datetime.now().strftime("%Y-%m-%d"),
        "Waste": waste,
        "Transport": transport,
        "Electricity": electricity,
        "Water": water_used,
        "Screen Time": screen_time,
        "Trees": tree_planted,
        **scores
    }

    try:
        log = pd.read_csv("eco_data.csv")
    except FileNotFoundError:
        log = pd.DataFrame()

    log = pd.concat([log, pd.DataFrame([entry])], ignore_index=True)
    log.to_csv("eco_data.csv", index=False)
    st.success("✅ Data saved for future analysis!")

    st.download_button("📁 Download Full CSV", data=log.to_csv(index=False), file_name="EcoLoopData.csv")

---

### 📌 Next Steps

Let me know and I can help you:
- Add **Streamlit Chatbot** using GPT API
- Add **CO₂ Sequestration Model** (like in your afforestation project)
- Add **Plastic Classifier** using AI and camera upload
- Convert this into a **research paper**

---

Would you like the **research paper template** or should I help you enhance this app with GPT integration or camera photo detection next?
