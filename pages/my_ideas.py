import streamlit as st

st.title("🔍 Project Marketplace")
st.write("Explore the latest startup ideas from our founders.")

default_ideas = [
    {"title": "EcoCharge", "industry": "Green Energy", "budget": 50000, "desc": "Solar-powered charging stations for electric bikes.", "founder": "Omar Farouk"},
    {"title": "HealthTrack AI", "industry": "Health", "budget": 120000, "desc": "AI assistant that predicts potential health risks.", "founder": "Laila Ahmed"},
    {"title": "SmartFarm", "industry": "AgriTech", "budget": 30000, "desc": "IOT sensors for automated irrigation.", "founder": "Youssef Hassan"},
    {"title": "CodeLearn", "industry": "EduTech", "budget": 15000, "desc": "Gamified platform for kids to learn Python.", "founder": "Nour Ibrahim"},
    {"title": "FinFlow", "industry": "Fintech", "budget": 200000, "desc": "Blockchain-based payment gateway.", "founder": "Ziad Mahmoud"},
    {"title": "QuickMeal", "industry": "FoodTech", "budget": 10000, "desc": "Healthy meal prep delivery based on DNA.", "founder": "Mariam Ali"},
    {"title": "VR-History", "industry": "EduTech", "budget": 45000, "desc": "Virtual Reality tours for ancient sites.", "founder": "Kareem Soliman"},
    {"title": "SafetyNet", "industry": "AI", "budget": 80000, "desc": "AI cameras for accidents detection.", "founder": "Samer Gamal"},
    {"title": "FitConnect", "industry": "Health", "budget": 25000, "desc": "Social network for local athletes.", "founder": "Hoda Mansour"},
    {"title": "AutoFix", "industry": "Tech", "budget": 60000, "desc": "On-demand mobile car repair service.", "founder": "Ahmed Abdo"}
]

if "db_ideas" not in st.session_state or len(st.session_state["db_ideas"]) == 0:
    st.session_state["db_ideas"] = default_ideas

for index, idea in enumerate(st.session_state["db_ideas"]):
    with st.container(border=True):
        col_text, col_img = st.columns([2, 1]) 
        with col_text:
            st.subheader(f"Project: {idea['title']}")
            st.markdown(f"**Industry:** {idea['industry']} | **Target:** ${idea.get('budget', 0):,}")
            st.write(idea['desc'])
            st.caption(f"👤 Founder: {idea['founder']}")
            st.button("View Details", key=f"btn_{index}")

        with col_img:
            if idea.get('image') is not None:
                st.image(idea['image'], use_container_width=True)
            else:
                st.image("https://cdn-icons-png.flaticon.com/512/6062/6062646.png", width=120)

st.divider()
if st.button("Back to Dashboard"):
    st.switch_page("menu.py")