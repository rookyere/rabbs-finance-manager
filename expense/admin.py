from django.contrib import admin
from .models import Expense, ExpenseType

# Register your models here.
admin.site.register(Expense)
admin.site.register(ExpenseType)
# admin.site.register(BudgetedExpense)
