from django.forms import ModelForm

from expenses.models import Expense


class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = [
            'expense_name',
            'expense_type',
            'amount',
            'currency',
            'date_added'
        ]