from django.db import models
from django.urls import reverse

# Create your models here.


class Expense(models.Model):
    exp_source = models.ForeignKey("ExpenseType", on_delete=models.CASCADE,verbose_name='Expense Category')
    exp_description = models.CharField("Description", max_length=200)
    exp_amount = models.DecimalField("Amount (Ghs)", max_digits=7, decimal_places=2, db_column="expense_amount")
    exp_date = models.DateField("Date of Expense", auto_now=False, auto_now_add=False)
    exp_date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.description}"


class Meta:
    db_table = "Expense"


class ExpenseType(models.Model):
    exp_source = models.CharField("Expense Category", max_length=50, unique=True, blank=False)

    def __str__(self):
        return f"{self.exp_source}"

    class Meta:
        db_table = "ExpenseType"
        ordering = ['exp_source']


# class BudgetedExpense(models.Model):
#     expense_category = models.ForeignKey('ExpenseCategory', on_delete=models.RESTRICT, default='Other')
#     description = models.CharField('Description', max_length=200)
#     budgeted_amount = models.DecimalField('Budgeted Amount (Ghs)', max_digits=19, decimal_places=2, db_column='Expense')
#     due_date = models.DateField('Due Date', auto_now=False, auto_now_add=False)
#     budget_period = models.CharField('Budget Month', max_length=200)

#     def __str__(self):
#         return f'{self.description} : Ghs{self.budgeted_amount}'
