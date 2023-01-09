from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    current_amount = models.DecimalField(max_digits=19, decimal_places=2)

class Transaction(models.Model):

    class Account_types(models.TextChoices):
        CONSUMPTION = 'consumption', 'Consumption'
        INCOME = 'income', 'Income'

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.IntegerField()
    type = models.CharField(max_length=15, choices=Account_types.choices, default=Account_types.CONSUMPTION)
    date = models.DateField(default=timezone.now)
    category = models.TextField(blank=True)

