import streamlit as st

# Initialize session states
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if 'name' not in st.session_state:
    st.session_state['name'] = None

if 'role' not in st.session_state:
    st.session_state['role'] = None

# If user is already logged in
if st.session_state['logged_in']:
    st.success(f"Welcome {st.session_state['name']} ({st.session_state['role']}) 🎉")

    if st.button("Go to Dashboard", use_container_width=True):
        st.switch_page("menu.py")

    if st.button("Log out"):
        st.session_state.clear()   
        st.rerun()

else:
    st.title("Sign In 🔑")
    st.write("Access Startup Connector")

    with st.form("signin_form"):
        email = st.text_input("Email", placeholder="example@gmail.com")
        password = st.text_input("Password", type="password")

        
        role = st.selectbox("Login as", ["Founder 🚀", "Sponsor 💰"])

        submit = st.form_submit_button("Sign In", use_container_width=True)

        if submit:
            if email and password:

                st.session_state['logged_in'] = True
                st.session_state['name'] = email.split("@")[0]
                st.session_state['role'] = role  

                st.success("Login successful 🎉")
                st.switch_page("menu.py")

            else:
                st.error("Please enter email and password")

    st.divider()
    st.write("Don't have an account?")

    if st.button("Sign Up Here", use_container_width=True):
        st.switch_page("signup.py")