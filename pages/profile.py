import streamlit as st


if not st.session_state.get('logged_in'):
    st.switch_page("signin.py")

st.title("👤 Profile")

name = st.text_input("Name")
skill = st.text_input("Skill")
education = st.text_input("Education")
bio = st.text_area("About You")

if st.button("Save"):
    st.session_state['name'] = name
    st.session_state['skill'] = skill
    st.session_state['education'] = education
    st.session_state['bio'] = bio
    st.success("Saved ✅")


if st.session_state.get('name'):
    st.divider()
    st.subheader("Your Info")

    st.write("Name:", st.session_state.get('name'))
    st.write("Skill:", st.session_state.get('skill'))
    st.write("Education:", st.session_state.get('education'))
    st.write("About:", st.session_state.get('bio'))
    role = st.session_state.get('role')
st.write("Role:", role)