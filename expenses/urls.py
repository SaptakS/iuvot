from django.urls import path

from expenses import views

urlpatterns = [
    path('add-expense', views.add_expense, name='add_expense'),
    path('expense-dashboard', views.view_expenses, name='expense_dashboard'),
]