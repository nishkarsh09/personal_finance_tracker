


from django.shortcuts import render, redirect 
from .models import Income
from .forms import IncomeForm

# Dashboard view (shows all income entries)
def dashboard(request):
    incomes = Income.objects.filter(user=request.user)  # Only show user's data
    total_income = sum(income.amount for income in incomes)
    return render(request, 'tracker/dashboard.html', {'incomes': incomes, 'total_income': total_income})

# Add Income view
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
    return render(request, 'tracker/add_income.html', {'form': form})

# Edit Income view
def edit_income(request, pk):
    income = Income.objects.get(pk=pk, user=request.user)
    if request.method == 'POST':
        form = IncomeForm(request.POST, instance=income)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = IncomeForm(instance=income)
    return render(request, 'tracker/edit_income.html', {'form': form})

# Delete Income view
def delete_income(request, pk):
    income = Income.objects.get(pk=pk, user=request.user)
    if request.method == 'POST':
        income.delete()
        return redirect('dashboard')
    return render(request, 'tracker/delete_income.html', {'income': income})
