# models.py
from django.db import models

class Expense(models.Model):
    person = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

  
