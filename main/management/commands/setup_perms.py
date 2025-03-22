from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from main.models import Transaction

class Command(BaseCommand):
    help = 'Create banking permission groups'

    def handle(self, *args, **kwargs):
        # Transaction permissions
        ct = ContentType.objects.get_for_model(Transaction)
        
        groups = {
            'Administrators': [
                'add_transaction', 'change_transaction', 
                'delete_transaction', 'view_transaction'
            ],
            'Fraud Team': [
                'change_transaction', 'view_transaction'
            ],
            'Customer Support': ['view_transaction']
        }

        for group_name, perms in groups.items():
            group, created = Group.objects.get_or_create(name=group_name)
            for codename in perms:
                perm = Permission.objects.get(codename=codename, content_type=ct)
                group.permissions.add(perm)
        
        self.stdout.write(self.style.SUCCESS('Banking groups created!'))
