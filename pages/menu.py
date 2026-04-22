import streamlit as st

# 🔒 حماية (لو مش عامل login)
if not st.session_state.get('logged_in'):
    st.switch_page("signin.py")

# 🧠 بيانات المستخدم
name = st.session_state.get("name")
role = st.session_state.get("role")

st.title(f"Dashboard 👋")
st.write(f"Welcome {name}")

st.divider()

# 🚀 Founder
if role == "Founder 🚀":
    st.subheader("🚀 Founder Options")

    if st.button("➕ Add Idea", use_container_width=True):
        st.switch_page("add_ideas.py")   # ✅ بدون pages

    if st.button("📊 My Ideas", use_container_width=True):
        st.switch_page("my_ideas.py")



# 💰 Sponsor
elif role == "Sponsor 💰":
    st.subheader("💰 Investor Options")

    if st.button("🔍 Browse Ideas", use_container_width=True):
        st.switch_page("browser_ideas.py")   # ✅ خليها زي اسم ملفك

    if st.button("⭐ Interested Ideas", use_container_width=True):
        st.switch_page("interested.py")


# 🤖 AI
st.divider()

if st.button("🤖 Talk with AI", use_container_width=True):
    st.switch_page("chatbot.py")

# 👤 Profile
if st.button("👤 Profile", use_container_width=True):
    st.switch_page("profile.py")

# 🚪 Logout
if st.button("🚪 Log out", use_container_width=True):
    st.session_state['logged_in'] = False
    st.session_state['name'] = None
    st.session_state['role'] = None
    st.rerun()