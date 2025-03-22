import os
import django
import requests
import json

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.core.management import call_command

# Initialize test database
call_command('migrate')

# API URL (Update if using different port)
API_URL = "http://localhost:8000/api/predict/"

# Sample transaction matching your columns
TEST_DATA = {
    "step": 45,
    "type": "TRANSFER",
    "amount": 1500000.00,
    "nameOrig": "C123456789",
    "oldbalanceOrg": 1500000.00,
    "newbalanceOrig": 0.00,
    "nameDest": "M987654321",
    "oldbalanceDest": 0.00,
    "newbalanceDest": 1500000.00
}

def test_prediction():
    try:
        response = requests.post(
            API_URL,
            json=TEST_DATA,
            headers={'Content-Type': 'application/json'}
        )
        response.raise_for_status()
        print("✅ Success:")
        print(json.dumps(response.json(), indent=2))
        
    except Exception as e:
        print("❌ Error:", str(e))

if __name__ == "__main__":
    test_prediction()
