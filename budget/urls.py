from django.urls import path
from .views import budget_item, delete_budget_item

urlpatterns = [
    path("", budget_item, name="budget"),
    path("budgetItem/<budget_item_id>", budget_item, name="update_budget_item"),
    path("deleteBudgetItem/<budget_item_id>", delete_budget_item, name="delete_budget_item")
]
