# import streamlit as st
# home_page = st.Page(page='home.py', title='Home Page', icon='🏡', default=True)
# profile_page = st.Page(page='profile.py', title='Profile Page', icon='👤')
# signin_page = st.Page(page='signin.py' , title='Sign In',icon='🔒')
# signup_page = st.Page(page='signup.py', title='Sign Up', icon='👤')
# chatbot_page = st.Page(page='chatbot.py', title='Talk With AI', icon='🤖')
# menu_page= st.Page(page='menu.py',title='menu',icon='📑')
# browser_ideas = st.Page(page="browser_ideas.py", title='browser yor ideas',icon='📝')
# intrested_ideas = st.Page(page="interested.py", title='interested ideas',icon='❤️')
# add_ideas= st.Page(page="add_ideas.py", title='add',icon='➕')
# my_ideas=st.Page(page="my_ideas.py", title='my ideas',icon='💭')

# all_pages = st.navigation( [home_page, profile_page, signin_page, signup_page,menu_page,browser_ideas,intrested_ideas,
#                             add_ideas,my_ideas ,chatbot_page],
#                           position='top')

# #run all pages
 
# all_pages.run()
import streamlit as st

st.set_page_config(page_title="Startup Hub", page_icon="🚀", layout="centered")

home_p = st.Page(page='home.py', title='Home Page', icon='🏡', default=True)
profile_p = st.Page(page='profile.py', title='Profile Page', icon='👤')
signin_p = st.Page(page='signin.py', title='Sign In', icon='🔒')
signup_p = st.Page(page='signup.py', title='Sign Up', icon='👤')
chatbot_p = st.Page(page='chatbot.py', title='Talk With AI', icon='🤖')
menu_p = st.Page(page='menu.py', title='Dashboard', icon='📊')
add_p = st.Page(page="add_ideas.py", title='Add Idea', icon='➕')
my_p = st.Page(page="my_ideas.py", title='My Ideas', icon='💭')

browse_p = st.Page(page="browser_ideas.py", title='Browse Ideas', icon='🔍')
interested_p = st.Page(page="interested.py", title='Interested Ideas', icon='❤️')

if not st.session_state.get('logged_in'):
    nav_pages = [home_p, signin_p, signup_p,menu_p, chatbot_p]
else:
    role = st.session_state.get('role')
    
    common_after_login = [home_p, menu_p, profile_p, chatbot_p]
    
    if role == "Founder 🚀":
   
        nav_pages = [home_p, menu_p, add_p, my_p, profile_p, chatbot_p,]
    
    elif role == "Sponsor 💰":
        
        nav_pages = [home_p, profile_p, browse_p, interested_p, chatbot_p,menu_p]
    
    else:
        nav_pages = common_after_login

all_pages = st.navigation(nav_pages, position='top')
all_pages.run()
