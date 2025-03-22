from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from main.models import BankUser

class Command(BaseCommand):
    help = 'Create banking system users with roles'
    
    ROLES = BankUser.Role.choices  # Get all available roles

    def handle(self, *args, **kwargs):
        users = [
            # System Administrator
            {
                'username': 'administrator',
                'password': 'Admin@123',
                'role': BankUser.Role.ADMIN,
                'branch': 'Mumbai-001',
                'is_staff': True,
                'is_superuser': True
            },
            # Fraud Manager
            {
                'username': 'fraud_operations_manager',
                'password': 'Admin@123',
                'role': BankUser.Role.FRAUD_MANAGER,
                'branch': 'Delhi-002',
                'is_staff': True,
                'is_superuser': False
            },
            # Customer Support
            {
                'username': 'support_executive',
                'password': 'Admin@123',
                'role': BankUser.Role.CUSTOMER_SUPPORT,
                'branch': 'Bangalore-003',
                'is_staff': True,
                'is_superuser': False
            },
            # Auditor
            {
                'username': 'normal_user',
                'password': 'Admin@123',
                'role': BankUser.Role.AUDITOR,
                'branch': 'Chennai-004',
                'is_staff': True,
                'is_superuser': False
            }
        ]

        for user_data in users:
            user, created = BankUser.objects.get_or_create(
                username=user_data['username'],
                defaults={
                    'role': user_data['role'],
                    'branch': user_data['branch'],
                    'employee_id': f"EMP-{user_data['role']}-001",
                    'is_staff': user_data['is_staff'],
                    'is_superuser': user_data['is_superuser']
                }
            )
            if created:
                user.set_password(user_data['password'])
                user.save()  # Triggers group assignment
                self.stdout.write(self.style.SUCCESS(f'Created {user.get_role_display()}: {user.username}'))
            else:
                self.stdout.write(self.style.WARNING(f'User {user_data["username"]} already exists'))
