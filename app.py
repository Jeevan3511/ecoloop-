import streamlit as st

# --- App Title ---
st.title("🌿 My Eco Score")
st.subheader("Discover how eco-friendly your habits are!")

# --- Questions and Options ---
questions = {
    "🌍 Earth (Waste)": ["I compost", "I use dustbins properly", "I litter sometimes", "I don't care"],
    "💧 Water (Usage)": ["Very minimal", "Average", "I waste water", "I don’t track"],
    "🔥 Fire (Travel)": ["Cycle/Walk", "Public transport", "Car/Bike", "Always by fuel vehicle"],
    "🌬️ Air (Electricity Use)": ["Mostly solar/LED", "Normal appliances", "Old high-power devices", "Very high usage"],
    "🌌 Space (Digital Life)": ["Use power-saving mode", "Normal usage", "Always online", "Never shut devices"]
}

scores = []

# --- Quiz Loop ---
st.write("### Answer the following:")
for question, options in questions.items():
    answer = st.radio(question, options, key=question)
    score = 0
    if answer == options[0]:
        score = 20
    elif answer == options[1]:
        score = 15
    elif answer == options[2]:
        score = 10
    else:
        score = 5
    scores.append(score)

# --- Calculate Eco Score ---
total_score = sum(scores)
st.write("### 🌱 Your Eco Score is:", total_score, "/ 100")

# --- Suggestions ---
st.write("### ✅ Simple Tips to Improve:")
suggestions = {
    "Earth": "Start composting or recycle daily waste.",
    "Water": "Close taps while brushing. Use water-efficient buckets.",
    "Fire": "Try cycling once a week. Reduce solo car rides.",
    "Air": "Switch to LED bulbs and unplug devices when not in use.",
    "Space": "Limit screen time and turn off unused devices."
}

for element, tip in suggestions.items():
    st.markdown(f"**{element} 🌟**: {tip}")

# --- Footer ---
st.markdown("---")
st.caption("Made with 💚 to help you grow greener with EcoLoop+")
