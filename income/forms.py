from django import forms
from django.forms import ModelForm
from .models import IncomeType, Income
from datetime import date
from django.utils.translation import gettext_lazy as wen
from django.core.exceptions import ValidationError
import re


class IncomeCatForm(ModelForm):
    class Meta:
        model = IncomeType
        fields = ["income_source"]
        # This is how to define labels for the forms
        # labels = {
        #     'income_source': ''
        # }

        widgets = {
            "income_source": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Provide source of Income",
                }
            )
        }


class IncomeItemForm(ModelForm):
    # def __ini__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     initial_choice = [('', 'Select source of income')]

    #     income_sources = IncomeType.objects.values_list('income_source',flat=True).distinct()
    #     source_choices = [(income_source, income_source) for income_source in income_sources]

    #     income_sources_choices = initial_choice + source_choices

    #     self.fields['income_source'].choices = income_sources_choices

    class Meta:
        model = Income
        fields = ["income_source", "description", "amount", "income_date"]
       
        widgets = {
            "income_source": forms.Select(attrs={"class": "form-select"}),
            "description": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Provide a description of source of Income",
                }
            ),
            # "amount": forms.DecimalField(max_digits=7, decimal_places=2),
            "amount": forms.TextInput(attrs={"class": "form-control"}),
            "income_date": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
        }

    def clean_income_date(self):
        data = self.cleaned_data["income_date"]

        if data > date.today():
            raise ValidationError("Date must be today or in the past")
        return data

    def clean_description(self):
        data = self.cleaned_data["description"].title()
    #     print(data)
    #     pattern = re.compile(r"")

    #     if not bool(re.search(pattern, data)):
    #         print(bool(re.match(pattern, data)))
    #         raise ValidationError("Description must be a word")
        return data

    # def clean_amount(self):
    #     data = self.cleaned_data['amount']

    #     if len(data.split('.')[1]) > 2:
    #         raise ValidationError('Invalid Amount. Value must be in 2 decimal places')
    #     return data
