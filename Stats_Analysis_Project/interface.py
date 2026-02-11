import streamlit as st
from PIL import Image
import Analysis 
from auth import login_user, create_user

# page configuration
st.set_page_config(page_title = "Rossman Sales Analysis Dashboard", 
                   page_icon = "chart_with_upwards_trend", 
                   layout = "wide",
                   initial_sidebar_state= "collapsed")

# initialize session state
def init_session():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if "username" not in st.session_state:
        st.session_state.username = ""
    
    if "page" not in st.session_state:
        st.session_state.page = "login"
        
init_session()

# load data
@st.cache_data
def load_data():
    df = Analysis.load_data()
    df = Analysis.preprocess_data(df)
    return df

# Dashboard
def dashboard():
    img = Image.open("images.jfif")
    st.image(img.resize((1000,200)))
    st.markdown("# Competetion Analysis Project")

    st.markdown("" \
        "<h2 style = 'text-align :center; font-weight:bold; color: red;' > ROSSMAN SALES ANALYSIS DASHBOARD </h2>" ,
        unsafe_allow_html = True)
    df = load_data()

    col1, col2 = st.columns([1, 4])

  # slider
    with col1:
        st.markdown("###  Controls")

        options = st.selectbox(
            "Select Analysis",
            [
                "Sales by Store Type",
                "Sales by Year",
                "Sales by Month",
                "Sales by Competition Distance",
                "Sales by Holiday"
            ]
        )
        
        st.markdown("_ _ _")
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.username = ""
            st.session_state.page = "login"
            st.rerun()

    # Main Area
    with col2:
        st.subheader(options)
        
        if options == "Sales by Store Type":
            fig = Analysis.sales_by_store(df)
            st.pyplot(fig)
            
        elif options == "Sales by Year":
            fig = Analysis.sales_by_year(df)
            st.pyplot(fig)
            
        elif options == "Sales by Month":
            fig = Analysis.sales_by_month(df)
            st.pyplot(fig)
            
        elif options == "Sales by Competition Distance":
            fig = Analysis.sales_by_competition_distance(df)
            st.pyplot(fig)
            
        elif options == "Sales by Holiday":
            fig = Analysis.sales_by_holiday(df)
            st.pyplot(fig)
            
# UI Design for Login and Signup            
def login_page():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        user = login_user(username, password)
        if user:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.page = "dashboard"
            st.success("Logged in successfully!")
            st.rerun()
        else:
            st.error("Invalid username or password")
            
    st.markdown("_ _ _")
    
    if st.button("Create an account"):
        st.session_state.page = "signup"
        st.rerun()

# signup page        
def signup_page():
    st.title("Sign Up")
    st.write("Create a new account")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Sign Up"):
            if username == "" or password == "":
                st.warning("All fields are required")
            else:
                create_user(username, password)
                st.success("User created successfully! Please login.")
                st.info("Go to Login page")
    with col2:
        if st.button("Go to Login"):
            st.session_state.page = "login"
            st.rerun()
                

# Main function
if st.session_state.logged_in and st.session_state.page == "dashboard":
    dashboard()
else:
    if st.session_state.page == "login":
        login_page()
    elif st.session_state.page == "signup":
        signup_page()