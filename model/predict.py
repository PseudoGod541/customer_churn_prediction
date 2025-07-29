import joblib
import pandas as pd
from tensorflow.keras.models import load_model
import os

# --- Global variables to store loaded models ---
preprocessor = None
model = None

def load_models():
    """Load the preprocessor and model once when the module is imported."""
    global preprocessor, model
    
    # Get the current directory of this script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    try:
        # Load the scikit-learn preprocessor
        preprocessor = joblib.load(os.path.join(current_dir, 'preprocessor.pkl'))
        # Load the trained Keras model
        model = load_model(os.path.join(current_dir, 'churn_model.h5'))
        print("Models loaded successfully!")
    except FileNotFoundError as e:
        raise RuntimeError("Model or preprocessor not found. Make sure 'preprocessor.pkl' and 'churn_model.h5' are in the model directory.") from e
    except Exception as e:
        raise RuntimeError(f"An error occurred while loading models: {e}") from e

def predict_churn_model(customer):
    """
    Predicts churn for a given customer.
    
    Args:
        customer: CustomerData object containing customer information
        
    Returns:
        dict: Contains prediction (0 or 1) and probability score
    """
    global preprocessor, model
    
    # Load models if not already loaded
    if preprocessor is None or model is None:
        load_models()
    
    # Convert the input Pydantic object to a pandas DataFrame
    # The model expects a 2D array, so we wrap the dict in a list
    input_df = pd.DataFrame([customer.dict()])

    # Ensure the column order is the same as during training
    # This is crucial for the preprocessor to work correctly
    try:
        # Extract feature names from the loaded preprocessor
        cat_features = preprocessor.transformers_[1][1].get_feature_names_out().tolist()
        num_features = preprocessor.transformers_[0][2]
        # Note: The above line for cat_features might differ slightly based on sklearn version.
        # A more robust way is to define the order explicitly if you know it.
        feature_order = ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure', 'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod', 'MonthlyCharges', 'TotalCharges']
        input_df = input_df[feature_order]

    except Exception as e:
        # Fallback if feature extraction fails
        print(f"Could not dynamically get feature names, using hardcoded order. Error: {e}")
        feature_order = ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure', 'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod', 'MonthlyCharges', 'TotalCharges']
        input_df = input_df[feature_order]

    # Transform the data using the loaded preprocessor
    encoded_data = preprocessor.transform(input_df)

    # Make a prediction using the loaded Keras model
    prediction_prob = model.predict(encoded_data)

    # Apply the same 0.6 threshold from your notebook
    churn_prediction = (prediction_prob[0][0] > 0.6).astype(int)

    # Return the final prediction and the probability score
    return {
        "prediction": int(churn_prediction),
        "probability": float(prediction_prob[0][0])
    }

# Load models when the module is imported
load_models()