from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from currency_converter import CurrencyConverter

from expenses.forms import ExpenseForm
from expenses.models import Expense


def view_expenses(request):
    expenses = Expense.objects.all()
    return render(request, 'expense_dashboard.html', {'expenses': expenses})

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        c = CurrencyConverter()
        if form.is_valid():
            expense = form.save(commit=False)
            expense.amount_in_inr = c.convert(expense.amount, expense.currency, 'INR')
            expense.save()
            return HttpResponseRedirect(reverse('expense_dashboard'))
    else:
        form = ExpenseForm()

    return render(request, 'expense_form.html', {'form': form})
