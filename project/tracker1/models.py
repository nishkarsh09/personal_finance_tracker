from django.db import models 
from django.contrib.auth.models import User 

class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    source = models.CharField(max_length=255)
    date = models.DateField()
    def __str__(self):
        return f"{self.source} - ${self.amount}"

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255)
    date = models.DateField()
    def __str__(self):
        return f"{self.category} - ${self.amount}"

class SavingsGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal_name = models.CharField(max_length=255)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_amount = models.DecimalField(max_digits=10, decimal_places=2)
    deadline = models.DateField()
    def __str__(self):
        return f"{self.target_amount} - ${self.current_amount} - ${self.goal_name}"


