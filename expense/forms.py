from django import forms
from django.forms import ModelForm
from .models import ExpenseType, Expense
from datetime import date
from django.utils.translation import gettext_lazy as wen
from django.core.exceptions import ValidationError
import re


class expenseCatForm(ModelForm):
    class Meta:
        model = ExpenseType
        fields = ["exp_source"]
        # This is how to define labels for the forms
        # labels = {
        #     'expense_source': ''
        # }

        widgets = {
            "exp_source": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Provide source of expense",
                }
            )
        }


class expenseItemForm(ModelForm):
    # def __ini__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     initial_choice = [('', 'Select source of expense')]

    #     expense_sources = expenseType.objects.values_list('expense_source',flat=True).distinct()
    #     source_choices = [(expense_source, expense_source) for expense_source in expense_sources]

    #     expense_sources_choices = initial_choice + source_choices

    #     self.fields['expense_source'].choices = expense_sources_choices

    class Meta:
        model = Expense
        fields = ["exp_source", "exp_description", "exp_amount", "exp_date"]

        widgets = {
            "exp_source": forms.Select(attrs={"class": "form-select"}),
            "exp_description": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Provide a description of source of expense",
                }
            ),
            "exp_amount": forms.TextInput(attrs={"class": "form-control"}),
            "exp_date": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
        }

    def clean_exp_date(self):
        data = self.cleaned_data["exp_date"]

        if data > date.today():
            raise ValidationError("Date must be today or in the past")
        return data

    def clean_exp_description(self):
        data = self.cleaned_data["exp_description"].title()
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
