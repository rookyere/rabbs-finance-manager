from django.urls import path
from .views import income_item, income_cat, delete_income_cat, delete_income_item

# app_name = 'income'

urlpatterns = [
    path("", income_item, name="income"),
    # path("addIncomeItem/", income_item, name='add_income_item'),
    path("incomeItem/<income_item_id>", income_item, name="update_income_item"),
    path(
        "deleteIncomeItem/<income_item_id>",
        delete_income_item,
        name="delete_income_item",
    ),
    path("incomeCategory/", income_cat, name="incomeCat"),
    path("updateIncomeCat/<income_cat_id>", income_cat, name="updateincomeCat"),
    path("deleteIncomeCat/<income_cat_id>", delete_income_cat, name="deleteincomeCat"),
]
