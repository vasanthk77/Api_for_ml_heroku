from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

# Create an instance of the FastAPI application
app = FastAPI()

# Define a Pydantic model for the input parameters
class ModelInput(BaseModel):
    CreditScore: int
    Age: int
    Tenure: int
    Balance: float
    NumOfProducts: int
    HasCrCard: int
    IsActiveMember: int
    EstimatedSalary: float
    Germany: int
    Spain: int
    Male: int

# Load the saved churn prediction model
churn_model = pickle.load(open('churn_model.sav', 'rb'))


@app.get('/Hello')
def hello():
    return {"welcome to the fastapis"}
# Define a route for making predictions
@app.post('/predict')
def churn_predict(input_parameters: ModelInput):
    input_data = input_parameters.dict()

    cs = input_data['CreditScore']
    ag = input_data['Age']
    tn = input_data['Tenure']
    bal = input_data['Balance']
    np = input_data['NumOfProducts']
    Hc = input_data['HasCrCard']
    Is = input_data['IsActiveMember']
    Sal = input_data['EstimatedSalary']
    Ger = input_data['Germany']
    Spa = input_data['Spain']
    Mal = input_data['Male']

    input_list = [cs, ag, tn, bal, np, Hc, Is, Sal, Ger, Spa, Mal]

    prediction = churn_model.predict([input_list])

    if prediction[0] == 0:
        return 'The person was continuing as a customer in the Bank....'
    else:
        return 'The person was closed his account in the Bank.....'
