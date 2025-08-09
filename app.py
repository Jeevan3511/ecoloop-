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

# ---------------------- KNOWLEDGE HUB (colorful card style) ----------------------
with tabs[5]:
    st.header("📚 Knowledge Hub — Learn · Get Inspired · Act")

    st.markdown("""
    <style>
    .kh-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 18px; }
    .kh-card {
        border-radius: 12px;
        padding: 16px;
        color: #072227;
        box-shadow: 0 6px 18px rgba(2,16,24,0.06);
        font-family: "Segoe UI", Roboto, Arial, sans-serif;
    }
    .kh-earth { background: linear-gradient(135deg,#e6f4ea,#d1f0d6); border-left: 6px solid #2e7d32; }
    .kh-water { background: linear-gradient(135deg,#e8f6ff,#dbeeff); border-left: 6px solid #0288d1; }
    .kh-fire  { background: linear-gradient(135deg,#fff4e6,#ffebd6); border-left: 6px solid #f57c00; }
    .kh-air   { background: linear-gradient(135deg,#f0fbff,#eaf8ff); border-left: 6px solid #00acc1; }
    .kh-space { background: linear-gradient(135deg,#f4ebff,#efe6ff); border-left: 6px solid #6a1b9a; }

    .kh-title { font-weight:700; font-size:18px; margin-bottom:6px; }
    .kh-sub { color:#234; margin-bottom:8px; }
    .kh-foot { margin-top:10px; font-size:13px; color:#123; opacity:0.8; }
    .kh-quote { background:#fff; padding:10px 12px; border-radius:8px; margin-top:8px; box-shadow: 0 3px 10px rgba(2,16,24,0.04); }
    .learn-btn { display:inline-block; margin-top:8px; padding:6px 10px; background:#ffffffcc; border-radius:8px; text-decoration:none; color:#000; font-weight:600; }
    </style>
    """ , unsafe_allow_html=True)

    st.markdown("<div class='kh-grid'>", unsafe_allow_html=True)

    # Earth card (Case study)
    st.markdown("""
    <div class='kh-card kh-earth'>
      <div class='kh-title'>🌱 Earth — Urban Afforestation (Case Study)</div>
      <div class='kh-sub'>Kakinada / East Godavari — community-driven coastal planting</div>
      <div>Local groups and schools planted native mangroves and native trees along coastlines and vacant lots. Result: improved shoreline stability and increased local biodiversity; projects combined planting with student-led monitoring and seedling nurseries.</div>
      <div class='kh-foot'>Lesson: Combine native-species planting with local stewardship and monitoring.</div>
      <a class='learn-btn' href='https://www.fao.org/forestry/home/en/' target='_blank'>Learn about native planting</a>
    </div>
    """, unsafe_allow_html=True)

    # Water card (Case study + fact)
    st.markdown("""
    <div class='kh-card kh-water'>
      <div class='kh-title'>💧 Water — Marine Cleanup & Detection</div>
      <div class='kh-sub'>Student coastal cleanups + AI detection pilots</div>
      <div>Example pilots use AI to flag high-plastic zones from drone/boat imagery, enabling targeted cleanups. Community groups turned collected plastic into upcycled products (benches, tiles).</div>
      <div class='kh-quote'>🔎 <b>Fact:</b> Marine debris often starts on land — stopping leaks (waste streams) upstream prevents ocean pollution.</div>
      <div class='kh-foot'>Action: Run a beach audit, map hotspots, and collaborate with local waste management.</div>
      <a class='learn-btn' href='https://theoceancleanup.com/' target='_blank'>Read an ocean cleanup project</a>
    </div>
    """, unsafe_allow_html=True)

    # Fire card (example + quick tip)
    st.markdown("""
    <div class='kh-card kh-fire'>
      <div class='kh-title'>🔥 Fire — Renewable Energy & Efficiency</div>
      <div class='kh-sub'>Solar microgrids and energy-efficiency campaigns</div>
      <div>Small solar microgrids (school rooftop arrays) combined with efficiency drives (LED swap, timers) deliver fast reductions in fossil-energy use and bills.</div>
      <div class='kh-quote'>💡 <b>Quick tip:</b> Replace 10 incandescent bulbs with LEDs → immediate ~60–80% lighting energy cut.</div>
      <div class='kh-foot'>Idea: Run an LED-swap drive and calculate campus payback time.</div>
      <a class='learn-btn' href='https://www.irena.org/' target='_blank'>Solar & renewables info</a>
    </div>
    """, unsafe_allow_html=True)

    # Air card (case study + stat)
    st.markdown("""
    <div class='kh-card kh-air'>
      <div class='kh-title'>🌬️ Air — Clean Mobility & Urban Health</div>
      <div class='kh-sub'>Bike-share and EV pilot programs</div>
      <div>City pilot programs that integrate bike lanes and shared e-bikes reduce short car trips. Fewer short car trips = measurable NO₂ and PM reductions in near-road neighborhoods.</div>
      <div class='kh-quote'>📊 <b>Stat:</b> Replacing short car trips with cycling can reduce a commuter's transport emissions by ~30–50%.</div>
      <div class='kh-foot'>Try: Organize 'car-free' days and a bike-to-campus challenge.</div>
      <a class='learn-btn' href='https://www.unep.org/resources' target='_blank'>UNEP resources</a>
    </div>
    """, unsafe_allow_html=True)

    # Space card (digital + orbital sustainability)
    st.markdown("""
    <div class='kh-card kh-space'>
      <div class='kh-title'>🌌 Space — Digital Footprint & Orbital Sustainability</div>
      <div class='kh-sub'>Cloud energy, e-waste recycling, and space-debris awareness</div>
      <div>Digital activities (cloud storage, video streaming, large AI workloads) consume electricity in data centers — reducing unnecessary storage and inefficient model runs lowers carbon. On the orbital side, tracking and responsibly deorbiting defunct satellites prevents long-term debris growth.</div>
      <div class='kh-quote'>🔭 <b>Example:</b> ESA and industry programs are testing technologies to remove or mitigate space debris while research reduces launch-related impacts.</div>
      <div class='kh-foot'>Action: Clean up old cloud storage, recycle old devices, and support space sustainability research.</div>
      <a class='learn-btn' href='https://www.esa.int' target='_blank'>ESA – space sustainability</a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # Inspirational Quotes Row (full width)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="display:flex; gap:12px; flex-wrap:wrap;">
      <div style="flex:1; min-width:220px; background:#fff7f0; border-left:6px solid #ff7043; padding:12px; border-radius:10px;">
        <b>💬 Quote</b><br><i>“The greatest threat to our planet is the belief that someone else will save it.”</i><br><small>— Robert Swan</small>
      </div>
      <div style="flex:1; min-width:220px; background:#f0fff4; border-left:6px solid #2e7d32; padding:12px; border-radius:10px;">
        <b>💬 Quote</b><br><i>“We do not inherit the Earth from our ancestors; we borrow it from our children.”</i><br><small>— Native American Proverb</small>
      </div>
      <div style="flex:1; min-width:220px; background:#f3f0ff; border-left:6px solid #6a1b9a; padding:12px; border-radius:10px;">
        <b>💬 Quote</b><br><i>“When we heal the Earth, we heal ourselves.”</i><br><small>— David Orr</small>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # Resources & quick actions
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="display:flex; gap:12px; flex-wrap:wrap;">
      <div style="background:#e8f5ff; padding:10px; border-radius:10px; min-width:220px;">
        <b>🔗 Quick Resource</b><br><a href='https://www.un.org/sustainable-development/' target='_blank'>UN Sustainable Development Goals</a>
      </div>
      <div style="background:#fff9e6; padding:10px; border-radius:10px; min-width:220px;">
        <b>🛠️ Action</b><br>Start a campus 'Plastic Audit' → document items, generate a clean-up plan.
      </div>
      <div style="background:#f0fff4; padding:10px; border-radius:10px; min-width:220px;">
        <b>📈 Tip</b><br>Run an energy audit: measure lights & appliances and identify top-3 savings.
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br><hr>", unsafe_allow_html=True)
    st.caption("Knowledge Hub — curated case studies, facts and practical actions to help you lead sustainability on campus.")
# ---------------------- FOOTER ----------------------
st.markdown("""
---
Made with ❤️ by JEEVAN MAGAPU | Promoting Sustainability | Inspired by the Five Elements 🌿
""")
