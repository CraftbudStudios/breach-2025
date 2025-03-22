# generate_test_data.py
import os
import django
import random
from decimal import Decimal, ROUND_HALF_UP

# Set the settings module (update 'your_project' to your actual Django project name if needed)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'antifraud.settings')
django.setup()

from main.models import Transaction

# Helper function to convert float to Decimal with two decimal places
def to_decimal(value):
    return Decimal(value).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

def generate_random_transaction():
    # Random step between 1 and 1000
    step = random.randint(1, 1000)
    # Transaction type
    transaction_types = ['CASH_IN', 'CASH_OUT', 'DEBIT', 'PAYMENT', 'TRANSFER']
    trans_type = random.choice(transaction_types)
    # Random amount between 10 and 10000
    amount = to_decimal(random.uniform(10.0, 10000.0))
    
    # Generate original name and destination name
    nameOrig = f"User{random.randint(1, 1000)}"
    nameDest = f"User{random.randint(1001, 2000)}"
    
    # Random balances for original account between 1000 and 50000
    oldbalanceOrg = to_decimal(random.uniform(1000.0, 50000.0))
    # If it's a debit-type transaction, subtract amount; else, add amount (simulate balance change)
    if trans_type in ['DEBIT', 'PAYMENT', 'TRANSFER']:
        newbalanceOrig = oldbalanceOrg - amount
    else:
        newbalanceOrig = oldbalanceOrg + amount

    # Random balances for destination account between 1000 and 50000
    oldbalanceDest = to_decimal(random.uniform(1000.0, 50000.0))
    # For incoming transactions, add amount; for outgoing, subtract amount
    if trans_type in ['CASH_IN', 'TRANSFER']:
        newbalanceDest = oldbalanceDest + amount
    else:
        newbalanceDest = oldbalanceDest - amount

    # Randomly determine if the transaction is fraudulent
    isFraud = random.choice([True, False])
    # If it's fraud, more likely to be flagged
    isFlaggedFraud = isFraud and (random.random() < 0.8)

    return Transaction(
        step=step,
        type=trans_type,
        amount=amount,
        nameOrig=nameOrig,
        oldbalanceOrg=oldbalanceOrg,
        newbalanceOrig=newbalanceOrig,
        nameDest=nameDest,
        oldbalanceDest=oldbalanceDest,
        newbalanceDest=newbalanceDest,
        isFraud=isFraud,
        isFlaggedFraud=isFlaggedFraud
    )

def generate_test_data(num_entries=100):
    transactions = [generate_random_transaction() for _ in range(num_entries)]
    Transaction.objects.bulk_create(transactions)
    print(f"{num_entries} transactions created successfully.")

if __name__ == '__main__':
    generate_test_data(100)
