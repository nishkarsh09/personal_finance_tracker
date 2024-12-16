from django.contrib import admin 
from .models import Income, Expense, SavingsGoal

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'source', 'date')
    search_fields = ('source',)
    list_filter = ('date',)

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'category', 'date')
    search_fields = ('category',)
    list_filter = ('date',)

@admin.register(SavingsGoal)
class SavingsGoalAdmin(admin.ModelAdmin):
    list_display = ('user', 'goal_name', 'target_amount', 'current_amount', 'deadline')
    search_fields = ('goal_name',)
    list_filter = ('deadline',)
