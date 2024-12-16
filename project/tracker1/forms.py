from django import forms 
from .models import Income, Expense, SavingsGoal
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['amount', 'source', 'date']

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['amount', 'category', 'date']

class SavingsGoalForm(forms.ModelForm):
    class Meta:
        model = SavingsGoal
        fields = ['goal_name', 'target_amount', 'current_amount', 'deadline']
