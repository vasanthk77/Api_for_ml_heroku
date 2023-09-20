import requests

# Define the URL of your FastAPI application
api_url = "http://127.0.0.1:8000/predict"  # Replace with your server URL

# Sample input data (modify this as needed)
input_data = {
    "CreditScore": 700,
    "Age": 35,
    "Tenure": 5,
    "Balance": 1500.0,
    "NumOfProducts": 2,
    "HasCrCard": 1,
    "IsActiveMember": 1,
    "EstimatedSalary": 50000.0,
    "Germany": 1,
    "Spain": 0,
    "Male": 1
}

# Send a POST request with the input data to the FastAPI endpoint
response = requests.post(api_url, json=input_data)

# Check the response from the API
if response.status_code == 200:
      result = response.text
      print("Prediction:", result)
else:
    print("Error:", response.status_code, response.text)
