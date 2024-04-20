from django.db import models
from django.urls import reverse

# Create your models here.


class Income(models.Model):
    income_source = models.ForeignKey("IncomeType", on_delete=models.CASCADE)
    # income_source = models.ForeignKey('IncomeType', on_delete=models.CASCADE, default='id')
    description = models.CharField("Description", max_length=200)
    amount = models.DecimalField("Amount (Ghs)", max_digits=7, decimal_places=2, db_column="Income")
    income_date = models.DateField(
        "Date Income Received", auto_now=False, auto_now_add=False
    )
    income_date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.description}"

    class Meta:
        db_table = "Income"


class IncomeType(models.Model):
    income_source = models.CharField(
        "Source of Income", max_length=50, unique=True, blank=False
    )

    def __str__(self):
        return f"{self.income_source}"

    class Meta:
        db_table = "IncomeType"