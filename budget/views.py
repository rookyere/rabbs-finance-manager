from django.shortcuts import render, redirect
from django.contrib import messages
from .models import BudgetExpense
from .forms import budgetItemForm
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator

# Create your views here.
def mypaginator(request, db_query):
    p = Paginator(db_query, 10)
    page = request.GET.get("page")
    cat_list = p.get_page(page)
    return cat_list


def budget_item(request, budget_item_id=None):
    cancel = "budget"
    if budget_item_id is None:
        action = "Add"
        # Create a new expense category
        if request.method == "POST":
            form = budgetItemForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Budget item has been addded successfully")
                return redirect("budget")
            else:
                # Initialize an emoty form for Get requests
                form = budgetItemForm(request.POST)
                # Get data from the database
                db_query = BudgetExpense.objects.all().order_by("-ext_expense_date",'-ext_date_time')
                # pass it to context
                context = {
                    "expense_list": mypaginator(request, db_query),
                    "form": form,
                    "cancel_url": cancel,
                    "action": action,
                }

                messages.error(request, "Invalid form submission.")
                # messages.error(request, form.errors)
                return render(request, "budget/budgetExpense.html", context)
        else:
            # Initialize an emoty form for Get requests
            form = budgetItemForm()
            # Get data from the database
            db_query = BudgetExpense.objects.all().order_by("-est_expense_date",'-est_date_time')
            # pass it to context
            context = {
                "expense_list": mypaginator(request, db_query),
                "form": form,
                "cancel_url": cancel,
                "action": action,
            }
            return render(request, "budget/budgetExpense.html", context)
    else:
        action = "Update"
        budget_expense_list_item = BudgetExpense.objects.get(pk=budget_item_id)
        form = budgetItemForm(request.POST or None, instance=budget_expense_list_item)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect("budget")
            else:
                # Initialize an emoty form for Get requests
                form = budgetItemForm(request.POST)
                # Get data from the database
                db_query = BudgetExpense.objects.all().order_by("-est_expense_date",'-est_date_time')
                # pass it to context
                context = {
                    "expense_list": mypaginator(request, db_query),
                    "form": form,
                    "cancel_url": cancel,
                    "action": action,
                }

                messages.error(request, "Invalid form submission.")
                # messages.error(request, form.errors)
                return render(request, "budget/budgetExpense.html", context)
        else:
            # Get data from the database
            db_query = BudgetExpense.objects.all().order_by("-est_expense_date",'-est_date_time')
            # pass it to context
            context = {
                "expense_list": mypaginator(request, db_query),
                "form": form,
                "cancel_url": cancel,
                "action": action,
            }
            return render(request, "budget/budgetExpense.html", context)


def delete_budget_item(request, budget_item_id):
    budget_item = BudgetExpense.objects.get(pk=budget_item_id)
    context = {
        "object_to_delete": budget_item,
        "cancel_url": "budget",
        "item_group": "budgeted expenses list",
    }
    if request.method == "GET":
        return render(request, "delete.html", context)
    if request.method == "POST":
        budget_item.delete()
        messages.success(
            request, f"{budget_item.est_description} has been deleted successfully"
        )
        return redirect("budget")

