from django.db import models
from datetime import date
from currency_converter import CurrencyConverter


class Expense(models.Model):
    c = CurrencyConverter()
    CURRENCIES = [(cur, cur) for cur in c.currencies]
    EXPENSE_TYPE = [
        ('IT', 'IT related things'),
        ('TR', 'Travel'),
        ('CS', 'Cash expense'),
        ('MS', 'Miscellenous'),
    ]

    expense_name = models.CharField(max_length=75)
    expense_type = models.CharField(
        max_length=2,
        choices=EXPENSE_TYPE,
        default='CS'
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(
        max_length=3,
        choices=CURRENCIES,
        default='INR'
    )
    amount_in_inr = models.DecimalField(max_digits=10, decimal_places=2)
    date_added = models.DateField(default=date.today)
