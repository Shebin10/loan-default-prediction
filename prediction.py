import streamlit as st
import base64
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import base64
import time



# Function to encode an image to Base64
def get_image_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Load background image
background_base64 = get_image_base64("loan.webp")  # Background image
image_base64 = get_image_base64("image.jpg")  # Image below the heading

# Page Config
st.set_page_config(page_title="Loan Default Prediction", page_icon="🏦", layout="wide")

# CSS for Styling
st.markdown(f"""
    <style>
        /* Full-page background image with reduced opacity */
        .stApp {{
            background: url("data:image/webp;base64,{background_base64}") no-repeat center center fixed;
            background-size: cover;
            background-color: rgba(255, 255, 255, 0.9);  /* White with 90% opacity */
            background-blend-mode: lighten;
        }}

        /* Title Styling */
        h1 {{
            text-align: center;
            font-size: 50px;
            font-weight: bold;
            background: linear-gradient(to right, #333333, #666666);
            -webkit-background-clip: text;
            color: transparent;
        }}

        /* Subheading */
        .subheading {{
            text-align: center;
            font-size: 22px;
            color: #555;
            margin-top: -10px;
        }}

        /* Center Image */
        .center-image {{
            display: flex;
            justify-content: center;
            margin-bottom: 20px;
        }}

        /* Custom Button */
        .custom-button {{
            display: block;
            margin: auto;
            padding: 12px 24px;
            font-size: 20px;
            font-weight: bold;
            color: white;
            background: linear-gradient(to right, #ff416c, #ff4b2b);
            border: none;
            border-radius: 25px;
            cursor: pointer;
            transition: all 0.3s ease;
        }}

        .custom-button:hover {{
            transform: scale(1.05);
            box-shadow: 0px 4px 15px rgba(255, 75, 43, 0.5);
        }}

        /* Footer */
        .footer {{
            text-align: center;
            color: #666;
            font-size: 16px;
            margin-top: 30px;
        }}
    </style>
    """, unsafe_allow_html=True)

# Initialize session state for navigation
if "page" not in st.session_state:
    st.session_state.page = "home"

# Function to navigate between pages
def go_to_prediction():
    st.session_state.page = "prediction"

# **Home Page**
if st.session_state.page == "home":
    st.markdown("<h1>Loan Default Prediction</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subheading'>Assess Loan Risk Using AI and Machine Learning</p>", unsafe_allow_html=True)
    st.markdown(f'<div class="center-image"><img src="data:image/webp;base64,{image_base64}" style="width: 500px;"></div>', unsafe_allow_html=True)

    # About Section
    st.markdown("""
        <h3 style="font-size: 20px;">About This Loan Risk Analyzer</h3>
        <p style="font-size: 16px; line-height: 1.6;">
            This Loan Default Prediction system uses <b>Machine Learning</b> to assess the risk of loan defaults. 
            By analyzing key financial and credit history details, the system predicts whether an individual is at 
            <b>high risk</b> or <b>low risk</b> of defaulting on their loan.
        </p>
        """, unsafe_allow_html=True)

    # How It Works
    st.markdown("""
        <h3 style="font-size: 20px;">How It Works</h3>
        <p style="font-size: 16px; line-height: 1.6;">
            1️⃣ Enter borrower details such as <b>income, credit history, loan amount, and more.</b><br>
            2️⃣ The model analyzes the data using <b>AI-powered algorithms.</b><br>
            3️⃣ The system predicts whether the borrower has a <b>High Risk</b> or <b>Low Risk</b> of defaulting.
        </p>
        """, unsafe_allow_html=True)

    # Navigation Button to Prediction Section
    st.button(" Predict Loan Default", on_click=go_to_prediction)

# **Prediction Page**
elif st.session_state.page == "prediction":
    def app():
        st.markdown("""
        <style>
             /* Remove top padding/margin and extend background */
            .block-container {
            padding-top: 0px !important;
            }
        
            /* Extend background color to the top */
            header[data-testid="stHeader"] {
             background-color: #26245E;  /* Match this with your existing background */
                height: 0px;  /* Shrinks the default white header */
            }
        </style>
            """, unsafe_allow_html=True)


        def get_image_base64(image_path):
            with open(image_path, "rb") as img_file:
             return base64.b64encode(img_file.read()).decode()

        image_base64 = get_image_base64("image1.webp")



        st.markdown(
            f"""
            <div style="display: flex; flex-direction: column; align-items: center; text-align: center;">
            <h1 style="background: linear-gradient(to right, #ffffff, #1e90ff);
                     -webkit-background-clip: text;
                    color: white;">
                LOAN DEFAULT PREDICTION
                </h1>
                <h3 style='color: gray;'>Assess Loan Risk with AI-Powered Predictions</h3>
                <img src="data:image/webp;base64,{image_base64}" style="width: 300px; margin-top: 10px;">
            </div>
            """,
        unsafe_allow_html=True)

 

        st.markdown(
            """<style>
                /* Main Background */
                .stApp {
                background: linear-gradient(to right, #0f0c29, #302b63, #24243e);
                color: white;
            }

            /* Centering the Image */
            .center-image {
                display: flex;
                justify-content: center;
                margin-bottom: 20px;
            }
            </style>""",
            unsafe_allow_html=True
        )

  
    
 


        # User input fields
        st.sidebar.markdown(
        "<h2 style='color: black;'>Enter the details to check loan default risk</h2>",
        unsafe_allow_html=True)

        age = st.sidebar.number_input("Age",min_value=18, max_value= 100, step = 1)
        income = st.sidebar.number_input("Annual Income ", step=1000)
        emp_length = st.sidebar.number_input("Years of Work Experience", 0, 45, 1)
        loan_grade = st.sidebar.selectbox("Select Loan Grade",  ["A", "B", "C", "D", "E"], index=0, 
                 help="Loan grade represents the creditworthiness of the borrower. 'A' is the highest grade(low risk)")
    
        loan_amount = st.sidebar.number_input("Loan Amount ", step=1000)
        loan_int_rate = st.sidebar.number_input("Loan Interest Rate (%)",  min_value=0.0,step=0.1, 
                    format="%.2f")
    
        loan_term = st.sidebar.number_input("Loan term in years",step=1)
        cred_hist_length = st.sidebar.number_input("Length of credit history in years",step=1)
        monthly_debt = st.sidebar.number_input("Monthly Debt ($)",  min_value=0.0,  step=50.0)
        num_active_loans = st.sidebar.number_input("Number of Active Loans",step=1)
        home_ownership = st.sidebar.selectbox("Home Ownership", ['RENT', 'OWN', 'MORTGAGE', 'OTHER'])
        loan_intent = st.sidebar.selectbox("Loan Purpose",
            ["Personal", "Education", "Medical Expenses", "Business", "Home Improvement", "Debt Consolidation"],
            index=0, help="Select the purpose for which the loan is being taken.") 

    
        rf = pickle.load(open('output/rf.sav', 'rb'))
        scaler = pickle.load(open('output/scaler_1.sav', 'rb'))
        le1 = pickle.load(open('output/grade_le.sav', 'rb'))
        ohe1 = pickle.load(open('output/owner_ohe.sav', 'rb'))
        ohe2 = pickle.load(open('output/intnt_ohe.sav', 'rb'))

        # Encoding categorical features
        grade_encoded = int(le1.transform([loan_grade])[0]) 
    
        ownership_encoded = ohe1.transform([[home_ownership]]).flatten()
        intent_encoded = ohe2.transform([[loan_intent]]).flatten()

        # Convert inputs to DataFrame
        features = np.concatenate(([age, income,emp_length, grade_encoded,loan_amount,loan_int_rate,
                    loan_term,cred_hist_length,monthly_debt,num_active_loans], ownership_encoded, intent_encoded)).reshape(1, -1)
        features_scaled = scaler.transform(features)

        # Predict
        st.markdown(
            """
            <style>
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap');

            body {
            background: linear-gradient(to right, #141e30, #243b55);
            color: white;
            font-family: 'Poppins', sans-serif;
            }

            @keyframes fadeIn {
             0% { opacity: 0; transform: scale(0.8); }
             100% { opacity: 1; transform: scale(1); }
            }

            .prediction-result {
             font-size: 36px;
             font-weight: bold;
             text-align: center;
             padding: 15px;
             border-radius: 10px;
             box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.3);
             animation: fadeIn 1s ease-in-out;
             width: 50%;
             margin: auto;
            }

            .high-risk {
             background-color: rgba(255, 0, 0, 0.2);
                color: red;
                border: 2px solid red;
            }

            .low-risk {
                background-color: rgba(0, 255, 0, 0.2);
                color: lime;
                border: 2px solid lime;
            }

            .footer {
                text-align: center;
                color: lightgray;
                font-size: 16px;
                margin-top: 20px;
            }

            .predict-button {
                display: block;
                margin: auto;
                padding: 10px 20px;
                font-size: 18px;
                font-weight: bold;
                color: white;
                background: linear-gradient(to right, #ff416c, #ff4b2b);
                border: none;
                border-radius: 25px;
                cursor: pointer;
                ransition: all 0.3s ease;
            }

            .predict-button:hover {
                transform: scale(1.05);
                box-shadow: 0px 4px 15px rgba(255, 75, 43, 0.5);
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        # Predict Button with Style
        if st.button("🔮 Predict Loan Default", key="predict", help="Click to predict", use_container_width=True):
            with st.spinner(" Analyzing loan risk... Please wait "):
                time.sleep(1.5)  # Simulating processing delay

            # Prediction Logic
            prediction = rf.predict(features_scaled)[0]


            # Display prediction result with styles
            if prediction == 0:
                st.markdown(
                 f'<div class="prediction-result high-risk"> High Risk of Default </div>',
                 unsafe_allow_html=True
             )
            else:
                st.markdown(
                    f'<div class="prediction-result low-risk"> Low Risk of Default </div>',
                    unsafe_allow_html=True
                )   

            


    app()
