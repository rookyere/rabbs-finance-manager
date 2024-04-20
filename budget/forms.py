from django import forms
from django.forms import ModelForm
from .models import BudgetExpense
from datetime import date
from django.core.exceptions import ValidationError
import re


class budgetItemForm(ModelForm):
    class Meta:
        model = BudgetExpense
        fields = ["est_expense_source", "est_description", "est_amount", "est_expense_date", "est_status"]

        widgets = {
            "est_expense_source": forms.Select(attrs={"class": "form-select"}),
            "est_description": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Provide a description of source of expense",
                }
            ),
            "est_amount": forms.TextInput(attrs={"class": "form-control"}),
            "est_expense_date": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "est_status": forms.Select(attrs={"class": "form-select"})
        }

    # def clean_est_expense_date(self):
    #     data = self.cleaned_data["est_expense_date"]

    #     if data > date.today():
    #         raise ValidationError("Date must be today or in the past")
    #     return data

    def clean_est_description(self):
        data = self.cleaned_data["est_description"].title()
        # print(data)
        # pattern = re.compile(r"")

        # if not bool(re.search(pattern, data)):
        #     print(bool(re.match(pattern, data)))
        #     raise ValidationError("Description must be a word")
        return data

    # def clean_amount(self):
    #     data = self.cleaned_data['amount']

    #     if len(data.split('.')[1]) > 2:
    #         raise ValidationError('Invalid Amount. Value must be in 2 decimal places')
    #     return data
