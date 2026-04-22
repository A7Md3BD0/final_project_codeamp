import streamlit as st

st.title("**:blue[sign up]**📝", text_alignment="center")

st.image(
    "https://th.bing.com/th/id/R.8cca65e79a1dffd8ec2215ae71069685?rik=tUBvCGuLQTwwPg&riu=http%3a%2f%2ffm.cnbc.com%2fapplications%2fcnbc.com%2fresources%2fimg%2feditorial%2f2014%2f01%2f07%2f101317308-show-thumb-sharktank-1600x900.1910x1000.jpg",
    caption="Join our family and build startups 🚀",
    use_container_width=True
)

st.write("Join Startup Connector 🚀")

with st.form("signup_form"):

    st.write("**:blue[Personal Information]**")

    role = st.radio(
        "Register as:",
        ["Founder 🚀", "Sponsor 💰"]
    )

    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("**:blue[Full Name]**")
        email = st.text_input("**:blue[Email]**", placeholder="example@gmail.com")
    with col2:
        phone = st.text_input("**:blue[Phone Number]**")
        password = st.text_input("**:blue[Password]**", type="password")

    st.write("**:blue[Profile Details]**")

    col3, col4 = st.columns([3, 1])
    with col3:
        address = st.text_input("**:blue[Address]**")
    with col4:
        national_id = st.text_input(
            "**:blue[National ID]**",
            placeholder="Enter your National ID"
        )

    submit = st.form_submit_button("Sign Up", use_container_width=True)

    if submit:
        if name and email and password and address and national_id:

            # Basic validation for national ID
            if not national_id.isdigit() or len(national_id) < 10:
                st.error("Invalid National ID ❌")
                st.stop()

            st.session_state['user'] = {
                "name": name,
                "email": email,
                "phone": phone,
                "address": address,
                "national_id": national_id,
                "role": role
            }

            st.success(f"Account created successfully for {name} 🎉")
            st.switch_page("signin.py")

        else:
            st.error("Please fill all required fields ❌")

st.divider()

st.write("Already have an account?")

if st.button("Sign In Here", use_container_width=True):
    st.switch_page("signin.py")