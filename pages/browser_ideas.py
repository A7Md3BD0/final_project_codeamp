import streamlit as st
import pandas as pd

# 🔒 حماية
if not st.session_state.get('logged_in'):
    st.switch_page("signin.py")

st.title("💰 Browse Startup Ideas")

st.success(f"Welcome {st.session_state.get('name')} 👋")

# 🧠 تجهيز requests
if 'requests' not in st.session_state:
    st.session_state['requests'] = []

# 💡 Data (تقدر بعد كده تجيبها من add_idea)
ideas = [
    {
        "title": "AI Fitness App",
        "desc": "AI generates workout plans",
        "budget": 50000,
        "owner": "Ahmed",
        "img": "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=600"
    },
    {
        "title": "Food Delivery Drone",
        "desc": "Delivery using drones",
        "budget": 120000,
        "owner": "Omar",
        "img": "https://images.unsplash.com/photo-1508615070457-7baeba4003ab?w=600"
    },
    {
        "title": "E-learning Platform",
        "desc": "Online courses system",
        "budget": 70000,
        "owner": "Hady",
        "img": "https://images.unsplash.com/photo-1584697964154-5c8c44b0d8d0?w=600"
    }
]

# 🧱 عرض زي المنيو (3 أعمدة)
col1, col2, col3 = st.columns(3)

for i, idea in enumerate(ideas):

    with [col1, col2, col3][i % 3]:

        st.image(idea["img"], use_container_width=True)
        st.subheader(idea["title"])
        st.write(idea["desc"])
        st.write(f"💰 Budget: {idea['budget']} EGP")
        st.write(f"👤 Founder: {idea['owner']}")

        if st.button(f"Interested 💰 {i}"):
            st.session_state['requests'].append({
                "idea": idea["title"],
                "owner": idea["owner"],
                "investor": st.session_state.get("name")
            })
            st.success("Request Sent ✅")

        st.divider()

# 📩 Summary (زي Order Summary)
st.subheader("📩 My Requests")

my_requests = [
    r for r in st.session_state['requests']
    if r["investor"] == st.session_state.get("name")
]

if len(my_requests) > 0:
    df = pd.DataFrame(my_requests)
    st.table(df)
else:
    st.info("No requests yet")