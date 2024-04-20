from django.urls import path
from .views import expense_item, expense_cat, delete_expense_cat, delete_expense_item

# app_name = 'expense'

urlpatterns = [
    path("", expense_item, name="expense"),
    # path("addexpenseItem/", expense_item, name='add_expense_item'),
    path("expenseItem/<expense_item_id>", expense_item, name="update_expense_item"),
    path(
        "deleteexpenseItem/<expense_item_id>",
        delete_expense_item,
        name="delete_expense_item",
    ),
    path("expenseCategory/", expense_cat, name="expenseCat"),
    path("updateexpenseCat/<expense_cat_id>", expense_cat, name="updateexpenseCat"),
    path(
        "deleteexpenseCat/<expense_cat_id>", delete_expense_cat, name="deleteexpenseCat"
    ),
]
