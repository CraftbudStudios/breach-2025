from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Transaction, BankUser

class BankUserAdmin(UserAdmin):
    list_display = ('username', 'role', 'branch', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Banking Info', {'fields': ('role', 'branch', 'employee_id')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    list_filter = ('role', 'branch')
    search_fields = ('username', 'employee_id')
    ordering = ('employee_id',)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('type', 'amount', 'nameOrig', 'nameDest', 'isFraud', 'prediction_timestamp')
    list_filter = ('type', 'isFraud')
    search_fields = ('nameOrig', 'nameDest')
    readonly_fields = ('prediction_timestamp',)
    ordering = ('-prediction_timestamp',)
    
    def has_delete_permission(self, request, obj=None):
        """Only allow admins to delete transactions"""
        return request.user.role == BankUser.Role.ADMIN
    
    def get_queryset(self, request):
        """Filter transactions based on user role"""
        qs = super().get_queryset(request)
        if request.user.role != BankUser.Role.ADMIN:
            return qs.filter(isFraud=False)
        return qs

admin.site.register(BankUser, BankUserAdmin)
