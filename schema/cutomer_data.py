from pydantic import BaseModel, Field
from typing import List, Literal, Annotated



# --- 3. Define the Input Data Model using Pydantic ---
# This ensures that the incoming data has the correct structure and types.
class CustomerData(BaseModel):
    gender: Annotated[Literal['Male', 'Female'], Field(description='Gender of the user')]
    SeniorCitizen: Annotated[Literal[0, 1], Field(description='Is the user a senior citizen?')]
    Partner: Annotated[Literal['Yes', 'No'], Field(description='Does the user have a partner?')]
    Dependents: Annotated[Literal['Yes', 'No'], Field(description='Does the user have dependents?')]
    tenure: Annotated[int, Field(gt=0, description='Tenure of the user in months')]
    PhoneService: Annotated[Literal['Yes', 'No'], Field(description='Does the user have phone service?')]
    MultipleLines: Annotated[Literal['No', 'No phone service', 'Yes'], Field(description='Does the user have multiple lines?')]
    InternetService: Annotated[Literal['Fiber optic', 'DSL', 'No'], Field(description='The user\'s internet service type')]
    OnlineSecurity: Annotated[Literal['No internet service', 'Yes', 'No'], Field(description='Does the user have online security?')]
    OnlineBackup: Annotated[Literal['No internet service', 'Yes', 'No'], Field(description='Does the user have online backup?')]
    DeviceProtection: Annotated[Literal['No internet service', 'Yes', 'No'], Field(description='Does the user have device protection?')]
    TechSupport: Annotated[Literal['No internet service', 'Yes', 'No'], Field(description='Does the user have tech support?')]
    StreamingTV: Annotated[Literal['No internet service', 'Yes', 'No'], Field(description='Does the user have streaming TV?')]
    StreamingMovies: Annotated[Literal['No internet service', 'Yes', 'No'], Field(description='Does the user have streaming movies?')]
    Contract: Annotated[Literal['Month-to-month', 'Two year', 'One year'], Field(description='The user\'s contract term')]
    PaperlessBilling: Annotated[Literal['Yes', 'No'], Field(description='Does the user use paperless billing?')]
    PaymentMethod: Annotated[Literal['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'], Field(description='The user\'s payment method')]
    MonthlyCharges: Annotated[float, Field(gt=0, description='Monthly charge for the user')]
    TotalCharges: float