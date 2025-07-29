import uvicorn
from fastapi import FastAPI, HTTPException
from schema.cutomer_data import CustomerData
from model.predict import predict_churn_model

# --- 1. Initialize FastAPI App ---
app = FastAPI(
    title="Telco Churn Prediction API",
    description="An API to predict customer churn using a trained Keras model.",
    version="1.0.0"
)

# --- 2. Define API Endpoints ---

# Root endpoint for a simple health check
@app.get("/")
def read_root():
    return {"status": "ok", "message": "Churn Prediction API is running."}

# Prediction endpoint
@app.post("/predict")
def predict_churn(customer: CustomerData):
    """
    Accepts customer data and returns a churn prediction.
    - **Prediction 0**: Customer will **not** churn.
    - **Prediction 1**: Customer **will** churn.
    """
    try:
        # Call the prediction function from model/predict.py
        result = predict_churn_model(customer)
        return result
    except Exception as e:
        # Raise an HTTPException for internal server errors
        raise HTTPException(status_code=500, detail=f"An error occurred during prediction: {str(e)}")

# --- 3. Run the application ---
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)