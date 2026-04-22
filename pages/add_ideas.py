import streamlit as st

st.title("🚀 Add New Idea")

if "db_ideas" not in st.session_state:
    st.session_state["db_ideas"] = []

with st.form("add_form", clear_on_submit=True):
    title = st.text_input("Project Name")
    industry = st.selectbox("Industry", ["AI", "Tech", "Health", "Fintech"])
    budget = st.number_input("Target Investment ($)", min_value=0)
    desc = st.text_area("Description")
    img = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])
    
    if st.form_submit_button("Publish"):
        if title and desc:
            new_idea = {"title": title, "industry": industry, "budget": budget, "desc": desc, "image": img, "founder": st.session_state.get('name', 'Ahmed Abdo')}
            st.session_state["db_ideas"].append(new_idea)
            st.success("Idea Published!")
        else:
            st.error("Fill all fields!")

if st.button("Back to Dashboard"):
    st.switch_page("menu.py")