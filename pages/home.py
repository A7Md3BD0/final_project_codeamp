import streamlit as st
st.title("**:rainbow[welcome to visual shark tank]** ",anchor=False , text_alignment='center')
st.markdown("***:blue[A STEP  TO SUCESS]***")
st.image("https://wallpaperaccess.com/full/12426928.jpg", use_container_width=True,caption="**:rainbow[step to sucess]**")
st.divider()    

col1,col2 = st.columns(2)
with col1:
    with st.container(border=True):
     st.image("https://tse1.mm.bing.net/th/id/OIP.duhdi2OPs_2RZE0S8YKIRQHaEs?rs=1&pid=ImgDetMain&o=7&rm=3" ,caption="**:rainbow[i want to invest]**", use_container_width=True  )
    if st.button("invest",use_container_width=True):
           st.switch_page("signin.py")
    with col2:
     with st.container(border=True):
      st.image("https://c8.alamy.com/comp/2H9BMR5/grunge-black-founder-word-with-star-icon-round-rubber-seal-stamp-on-white-background-2H9BMR5.jpg" ,caption="**:rainbow[i want to pitch]**", use_container_width=True  )    
     if st.button("pitch",use_container_width=True):
       st.switch_page("signin.py")