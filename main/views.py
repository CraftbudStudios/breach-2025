from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Transaction
import json
import joblib
import pandas as pd
import numpy as np

# Load pre-trained model and preprocessor (add error handling)
try:
    model = joblib.load('fraud_model.joblib')
    preprocessor = joblib.load('preprocessor.joblib')
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

@csrf_exempt  # Remove in production!
def predict_fraud(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # Create transaction record
            transaction = Transaction.objects.create(
                step=data.get('step'),
                type=data.get('type'),
                amount=data.get('amount'),
                nameOrig=data.get('nameOrig'),
                oldbalanceOrg=data.get('oldbalanceOrg'),
                newbalanceOrig=data.get('newbalanceOrig'),
                nameDest=data.get('nameDest'),
                oldbalanceDest=data.get('oldbalanceDest'),
                newbalanceDest=data.get('newbalanceDest'),
                isFraud=False  # Default until prediction
            )
            
            # Prepare features for model
            features = pd.DataFrame([{
                'step': data['step'],
                'type': data['type'],
                'amount': data['amount'],
                'oldbalanceOrg': data['oldbalanceOrg'],
                'newbalanceOrig': data['newbalanceOrig'],
                'oldbalanceDest': data['oldbalanceDest'],
                'newbalanceDest': data['newbalanceDest']
            }])
            
            # Transform features
            processed_features = preprocessor.transform(features)
            
            # Get prediction
            is_fraud = model.predict(processed_features)[0]
            fraud_prob = model.predict_proba(processed_features)[0][1]
            
            # Update transaction with prediction
            transaction.isFraud = bool(is_fraud)
            transaction.save()
            
            return JsonResponse({
                'fraud_prediction': is_fraud,
                'confidence': float(fraud_prob),
                'transaction_id': transaction.id
            })
            
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid method'}, status=405)
