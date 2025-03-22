from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, Group, Permission

class BankUser(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'System Administrator'
        FRAUD_MANAGER = 'FRAUD', 'Fraud Manager'
        CUSTOMER_SUPPORT = 'SUPPORT', 'Customer Support'
        AUDITOR = 'AUDIT', 'Auditor'

    role = models.CharField(max_length=7, choices=Role.choices, default=Role.CUSTOMER_SUPPORT)
    branch = models.CharField(max_length=50)
    employee_id = models.CharField(max_length=20, unique=True)
    last_password_change = models.DateTimeField(auto_now_add=True)
    
    # Required fields
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # Fix permission clashes
    groups = models.ManyToManyField(
        Group,
        related_name='bankuser_set',
        related_query_name='bankuser',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='bankuser_set',
        related_query_name='bankuser',
        blank=True
    )
    def _assign_default_group(self):
        group_mapping = {
            self.Role.ADMIN: 'Administrators',
            self.Role.FRAUD_MANAGER: 'Fraud Team',  # Match setup_perms
            self.Role.CUSTOMER_SUPPORT: 'Customer Support',
            self.Role.AUDITOR: 'Auditors'
        }

    def save(self, *args, **kwargs):
        # Save first to get ID for M2M relationships
        super().save(*args, **kwargs)
        self._assign_default_group()

    def _assign_default_group(self):
        group_mapping = {
            self.Role.ADMIN: 'Administrators',
            self.Role.FRAUD_MANAGER: 'Fraud Team',
            self.Role.CUSTOMER_SUPPORT: 'Customer Support',
            self.Role.AUDITOR: 'Auditors'
        }
        group_name = group_mapping.get(self.role)
        
        if group_name:
            group, _ = Group.objects.get_or_create(name=group_name)
            self.groups.add(group)
    def __str__(self):
        return f"{self.employee_id} - {self.get_role_display()}"

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
