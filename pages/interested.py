import streamlit as st

import pandas as pd

# 🔒 حماية

if not st.session_state.get('logged_in'):

    st.switch_page("signin.py")

st.title("⭐ Interested Ideas")

st.success(f"Hello {st.session_state.get('name')} 👋")

# 🧠 لو مفيش requests

if 'requests' not in st.session_state:

    st.session_state['requests'] = []

# 🔍 فلترة على المستخدم الحالي

my_requests = [

    r for r in st.session_state['requests']

    if r["investor"] == st.session_state.get("name")

]

# 💡 عرض الأفكار بنفس شكل cards

if len(my_requests) > 0:

    cols = st.columns(3)

    for i, idea in enumerate(my_requests):

        with cols[i % 3]:

            st.subheader(idea["idea"])

            st.write(f"👤 Founder: {idea['owner']}")

            # زرار حذف (زي remove من cart)

            if st.button(f"❌ Remove {i}"):

                st.session_state['requests'].remove(idea)

                st.rerun()

            st.divider()

else:

    st.info("You have no interested ideas yet 😢")

# 📊 Summary زي المنيو

st.divider()

st.subheader("📊 Summary")

st.write(f"Total Interested Ideas: {len(my_requests)}")