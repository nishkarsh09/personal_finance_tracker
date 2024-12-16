

from django.shortcuts import render, redirect 
from .models import Income,Expense,SavingsGoal
from .forms import IncomeForm
from .forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login.html')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


# Dashboard view (shows all income entries)
@login_required
def dashboard(request):
    incomes = Income.objects.filter(user=request.user)  # Only show user's data
    expense_list = Expense.objects.filter(user=request.user)
    savings_goals = SavingsGoal.objects.filter(user=request.user)
    total_income = sum(income.amount for income in incomes)
    return render(request, 'dashboard.html', {'incomes': incomes, 'total_income': total_income,'expense_list': expense_list,'savings_goals': savings_goals})

# Add Income view
@login_required
def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user
            income.save()
            return redirect('dashboard')
    else:
        form = IncomeForm()
    return render(request, 'add_income.html', {'form': form})

# Edit Income view
@login_required
def edit_income(request, pk):
    income = Income.objects.get(pk=pk, user=request.user)
    if request.method == 'POST':
        form = IncomeForm(request.POST, instance=income)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = IncomeForm(instance=income)
    return render(request, 'edit_income.html', {'form': form})

# Delete Income view
@login_required
def delete_income(request, pk):
    income = Income.objects.get(pk=pk, user=request.user)
    if request.method == 'POST':
        income.delete()
        return redirect('dashboard')
    return render(request, 'delete_income.html', {'income': income})
