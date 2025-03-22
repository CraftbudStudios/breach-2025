from django.core.management.base import BaseCommand
from models import Transaction
import random
from decimal import Decimal

class Command(BaseCommand):
    help = 'Populate the database with sample transactions'

    def handle(self, *args, **options):
        transaction_types = ['CASH_IN', 'CASH_OUT', 'DEBIT', 'PAYMENT', 'TRANSFER']

        for _ in range(100):
            Transaction.objects.create(
                step=random.randint(1, 1000),
                type=random.choice(transaction_types),
                amount=Decimal(random.uniform(10, 1000000)).quantize(Decimal('0.01')),
                nameOrig=f'C{random.randint(100000, 999999)}',
                oldbalanceOrg=Decimal(random.uniform(0, 1000000)).quantize(Decimal('0.01')),
                newbalanceOrig=Decimal(random.uniform(0, 1000000)).quantize(Decimal('0.01')),
                nameDest=f'M{random.randint(100000, 999999)}',
                oldbalanceDest=Decimal(random.uniform(0, 1000000)).quantize(Decimal('0.01')),
                newbalanceDest=Decimal(random.uniform(0, 1000000)).quantize(Decimal('0.01')),
                isFraud=random.choice([True, False]),
                isFlaggedFraud=random.choice([True, False]),
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with 100 sample transactions'))
