# End-to-End Customer Churn Prediction Application

This project is a full-stack application designed to predict customer churn for a telecommunications company. It includes a machine learning model, a RESTful API backend, a user-friendly web interface, and is fully containerized with Docker for easy deployment.



---

## 📋 Features

-   **ML Model**: A robust model trained on the Telco Customer Churn dataset to predict churn probability.
-   **FastAPI Backend**: A high-performance REST API to serve predictions in real-time.
-   **Streamlit Frontend**: An interactive web interface for easy user interaction and demonstration.
-   **Dockerized**: The entire application (backend and frontend) is containerized using Docker and managed with Docker Compose for seamless setup and deployment.
-   **Business Insights**: The API provides actionable recommendations based on the prediction to help reduce churn.

---

## 🛠️ Tech Stack

-   **Backend**: Python, FastAPI, Uvicorn
-   **Machine Learning**: Scikit-learn, TensorFlow, Pandas, NumPy
-   **Frontend**: Streamlit, Requests
-   **Deployment**: Docker, Docker Compose

---

## 🚀 How to Run

To run this application, you need to have Docker and Docker Compose installed on your machine.
```bash
### 1. Clone the Repository


git clone <your-repository-url>
cd <your-project-directory>

2. Place Model Files
Ensure your trained model files are placed inside a models/ directory in the root of the project. This includes:

preprocessor.pkl

churn_model.h5 (or your saved model file)

Any other required model assets.

3. Run with Docker Compose
This single command will build the Docker image and start both the FastAPI backend and the Streamlit frontend.

docker-compose up --build

4. Access the Application
Once the containers are running, you can access the services:

Streamlit Frontend: Open your browser and go to http://localhost:8501

FastAPI Backend Docs: Open your browser and go to http://localhost:8000/docs

📁 Project Structure
.
├── models/               # Contains trained model and preprocessor
├── main.py               # FastAPI application
├── streamlit_app.py      # Streamlit frontend application
├── Dockerfile            # Instructions to build the Docker image
├── docker-compose.yml    # Defines and runs the multi-container setup
├── .dockerignore         # Specifies files to ignore during build
└── requirements.txt      # Python dependencies
