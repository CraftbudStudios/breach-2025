from django.db import models

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('CASH_IN', 'Cash In'),
        ('CASH_OUT', 'Cash Out'),
        ('DEBIT', 'Debit'),
        ('PAYMENT', 'Payment'),
        ('TRANSFER', 'Transfer'),
    ]
    
    step = models.IntegerField()
    type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    nameOrig = models.CharField(max_length=50)
    oldbalanceOrg = models.DecimalField(max_digits=15, decimal_places=2)
    newbalanceOrig = models.DecimalField(max_digits=15, decimal_places=2)
    nameDest = models.CharField(max_length=50)
    oldbalanceDest = models.DecimalField(max_digits=15, decimal_places=2)
    newbalanceDest = models.DecimalField(max_digits=15, decimal_places=2)
    isFraud = models.BooleanField(default=False)
    isFlaggedFraud = models.BooleanField(default=False)
    prediction_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type} - {self.amount}"
