import requests
import json
url = 'https://9a2e-34-168-123-160.ngrok-free.app/diabetes_prediction'

input_data_for_model = {
    
    'Pregnancies' : 6,
    'Glucose' : 148,
    'BloodPressure' : 72,
    'SkinThickness' : 35,
    'Insulin' : 0,
    'BMI' : 33.6,
    'DiabetesPedigreeFunction' : 0.627,
    'Age' : 50
    
    }

input_json = json.dumps(input_data_for_model)

response = requests.post(url, data=input_json)

if response.status_code == 200:
    print(response.text)  
else:
    print(f"Error: {response.status_code} - {response.text}")  


