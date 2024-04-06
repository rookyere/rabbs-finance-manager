from django.db import models
from expense.models import ExpenseType
# Create your models here.

status = (
        ("Budget assigned", "Budget assigned"),
        ("Completed", "Completed"),
        ("Pending budget", "Pending budget"),
    )

class BudgetExpense(models.Model):
    est_expense_source = models.ForeignKey(ExpenseType, on_delete=models.CASCADE,verbose_name='Expense Category')
    est_description = models.CharField("Description", max_length=100)
    est_amount = models.DecimalField("Estimated Expense Amount (Ghs)", max_digits=7, decimal_places=2, db_column="budget_expense_amt")
    est_expense_date = models.DateField("Estimated Date of Expense", auto_now=False, auto_now_add=False)
    est_date_time = models.DateTimeField(auto_now_add=True)
    est_status = models.CharField("Status", max_length=50,choices=status, default='Pending budget')

    def __str__(self):
        return f"{self.est_description}"


class Meta:
    db_table = "ExpenseBudget"