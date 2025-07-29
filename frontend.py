import streamlit as st
import requests
import json

# --- Page Configuration ---
st.set_page_config(
    page_title="Telco Churn Prediction",
    page_icon="📡",
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- FastAPI Backend URL ---
# Make sure your FastAPI server is running at this address
API_URL = "http://api:8000/predict"

# --- UI Design ---
st.title("Telco Customer Churn Prediction 🔮")
st.write(
    "This app predicts whether a customer is likely to churn based on their "
    "account information. Please provide the customer's details in the sidebar."
)

# --- Sidebar for User Inputs ---
st.sidebar.header("Customer Information")

def get_user_inputs():
    """Creates sidebar widgets and returns a dictionary of user inputs."""
    
    # --- Input fields are created based on the FastAPI's Pydantic model ---
    gender = st.sidebar.selectbox('Gender', ('Male', 'Female'))
    senior_citizen = st.sidebar.selectbox('Senior Citizen', (0, 1), format_func=lambda x: 'Yes' if x == 1 else 'No')
    partner = st.sidebar.selectbox('Partner', ('Yes', 'No'))
    dependents = st.sidebar.selectbox('Dependents', ('Yes', 'No'))
    
    st.sidebar.markdown("---")
    
    tenure = st.sidebar.slider('Tenure (months)', 1, 72, 12)
    phone_service = st.sidebar.selectbox('Phone Service', ('Yes', 'No'))
    multiple_lines = st.sidebar.selectbox('Multiple Lines', ('No', 'No phone service', 'Yes'))
    internet_service = st.sidebar.selectbox('Internet Service', ('Fiber optic', 'DSL', 'No'))
    
    st.sidebar.markdown("---")
    
    online_security = st.sidebar.selectbox('Online Security', ('No internet service', 'Yes', 'No'))
    online_backup = st.sidebar.selectbox('Online Backup', ('No internet service', 'Yes', 'No'))
    device_protection = st.sidebar.selectbox('Device Protection', ('No internet service', 'Yes', 'No'))
    tech_support = st.sidebar.selectbox('Tech Support', ('No internet service', 'Yes', 'No'))
    streaming_tv = st.sidebar.selectbox('Streaming TV', ('No internet service', 'Yes', 'No'))
    streaming_movies = st.sidebar.selectbox('Streaming Movies', ('No internet service', 'Yes', 'No'))
    
    st.sidebar.markdown("---")
    
    contract = st.sidebar.selectbox('Contract', ('Month-to-month', 'Two year', 'One year'))
    paperless_billing = st.sidebar.selectbox('Paperless Billing', ('Yes', 'No'))
    payment_method = st.sidebar.selectbox('Payment Method', ('Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'))
    
    monthly_charges = st.sidebar.number_input('Monthly Charges ($)', min_value=18.0, max_value=120.0, value=70.0, step=0.1)
    total_charges = st.sidebar.number_input('Total Charges ($)', min_value=18.0, max_value=8700.0, value=1500.0, step=1.0)

    # Create a dictionary from the inputs
    data = {
        "gender": gender,
        "SeniorCitizen": senior_citizen,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone_service,
        "MultipleLines": multiple_lines,
        "InternetService": internet_service,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless_billing,
        "PaymentMethod": payment_method,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges
    }
    return data

# Get inputs from the user
user_data = get_user_inputs()

# --- Prediction Logic ---
if st.button('Predict Churn', key='predict_button'):
    # Show a spinner while waiting for the API response
    with st.spinner('Sending data to the model...'):
        try:
            # Convert data to JSON and send the POST request
            response = requests.post(API_URL, data=json.dumps(user_data), headers={'Content-Type': 'application/json'})
            response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

            result = response.json()
            prediction = result.get('prediction')
            probability = result.get('probability')

            st.subheader("Prediction Result")
            if prediction == 1:
                st.error(f"**Prediction: Customer Will Churn**")
                st.write(f"Confidence: {probability*100:.2f}%")
                st.progress(probability)
            else:
                st.success(f"**Prediction: Customer Will Not Churn**")
                st.write(f"Confidence of Not Churning: {(1-probability)*100:.2f}%")
                st.progress(1 - probability)

        except requests.exceptions.RequestException as e:
            st.error(f"Could not connect to the API. Please make sure the FastAPI server is running. Error: {e}")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")

# --- Display Raw Data (Optional) ---
if st.checkbox('Show raw input data'):
    st.subheader('Raw Input Data')
    st.json(user_data)