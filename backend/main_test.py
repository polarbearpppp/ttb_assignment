import requests
import json
import os


# The URL where your FastAPI is running
BASE_URL = os.getenv("API_URL", "http://localhost:8000")

# Define different test cases
with open('backend/test_case.json', 'r') as f:
    # Parsing the JSON file into a Python dictionary
    test_cases = json.load(f)

def run_tests():
    print("--- STARTING API TESTS ---\n")
    
    for case in test_cases:
        print(f"Scenario: {case['name']}")
        
        try:
            # Send the POST request
            response = requests.post(f"{BASE_URL}/predict", json=case['feature'])
            
            # Print status and result
            if response.status_code == 200:
                result = response.json()
                print(f"✅ Success!")
                print(f"   Customer ID: {result['customer_id']}")
                print(f"   Prediction:  {result['prediction']}")
                print(f"   Confidence:  {result['confidence']}")
            else:
                print(f"❌ Failed! Status Code: {response.status_code}")
                print(f"   Message: {response.text}")
                
        except Exception as e:
            print(f"Error connecting to server: {e}")
            
        print("-" * 30)


run_tests()