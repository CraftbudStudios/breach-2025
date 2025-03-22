from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('type', 'amount', 'nameOrig', 'nameDest', 'isFraud', 'prediction_timestamp')
    list_filter = ('type', 'isFraud')
    search_fields = ('nameOrig', 'nameDest')
    readonly_fields = ('prediction_timestamp',)
    ordering = ('-prediction_timestamp',)
