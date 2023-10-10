from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Expense, ExpenseType
from .forms import expenseCatForm, expenseItemForm
from django.core.paginator import Paginator

# Create your views here.
def mypaginator(request, db_query):
    p = Paginator(db_query, 10)
    page = request.GET.get("page")
    cat_list = p.get_page(page)
    return cat_list


def expense_item(request, expense_item_id=None):
    cancel = "expense"
    if expense_item_id is None:
        action = "Add"
        # Create a new expense category
        if request.method == "POST":
            form = expenseItemForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Expense item has been addded successfully")
                return redirect("expense")
            else:
                # Initialize an emoty form for Get requests
                form = expenseItemForm(request.POST)
                # Get data from the database
                db_query = Expense.objects.all().order_by("-exp_date",'-exp_date_time')
                # pass it to context
                context = {
                    "expense_list": mypaginator(request, db_query),
                    "form": form,
                    "cancel_url": cancel,
                    "action": action,
                }

                messages.error(request, "Invalid form submission.")
                # messages.error(request, form.errors)
                return render(request, "expense/expenses.html", context)
        else:
            # Initialize an emoty form for Get requests
            form = expenseItemForm()
            # Get data from the database
            db_query = Expense.objects.all().order_by("-exp_date",'-exp_date_time')
            # pass it to context
            context = {
                "expense_list": mypaginator(request, db_query),
                "form": form,
                "cancel_url": cancel,
                "action": action,
            }
            # print(context['expense_list'])
            return render(request, "expense/expenses.html", context)
    else:
        action = "Update"
        expense_list_item = Expense.objects.get(pk=expense_item_id)
        form = expenseItemForm(request.POST or None, instance=expense_list_item)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect("expense")
            else:
                # Initialize an emoty form for Get requests
                form = expenseItemForm(request.POST)
                # Get data from the database
                db_query = Expense.objects.all().order_by("-exp_date",'-exp_date_time')
                # pass it to context
                context = {
                    "expense_list": mypaginator(request, db_query),
                    "form": form,
                    "cancel_url": cancel,
                    "action": action,
                }

                messages.error(request, "Invalid form submission.")
                # messages.error(request, form.errors)
                return render(request, "expense/expenses.html", context)
        else:
            # Get data from the database
            db_query = Expense.objects.all().order_by("-exp_date",'-exp_date_time')
            # pass it to context
            context = {
                "expense_list": mypaginator(request, db_query),
                "form": form,
                "cancel_url": cancel,
                "action": action,
            }
            return render(request, "expense/expenses.html", context)


def delete_expense_item(request, expense_item_id):
    expense_item = Expense.objects.get(pk=expense_item_id)
    context = {
        "object_to_delete": expense_item,
        "cancel_url": "expense",
        "item_group": "list of expense",
    }
    if request.method == "GET":
        return render(request, "delete.html", context)
    if request.method == "POST":
        expense_item.delete()
        messages.success(
            request, f"{expense_item.description} has been deleted successfully"
        )
        return redirect("expense")


def expense_cat(request, expense_cat_id=None):
    cancel = "expenseCat"
    if expense_cat_id is None:
        action = "Add"
        # Create a new expense category
        if request.method == "POST":
            form = expenseCatForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(
                    request, f"expense Category has been created successfully"
                )
                return redirect("expenseCat")
            else:
                 # Initialize an emoty form for Get requests
                form = expenseCatForm()
                # Get data from the database
                db_query = ExpenseType.objects.all().order_by("exp_source")
                # pass it to context
                context = {
                "cat_list": mypaginator(request, db_query),
                "form": form,
                "cancel_url": cancel,
                "action": action,
                }
                # messages.error(request, "Invalid form submission.")
                messages.error(request, form.errors)
                return render(request, "expense/expenseCat.html", context)
                
                
        else:
            # Initialize an emoty form for Get requests
            form = expenseCatForm()
            # Get data from the database
            db_query = ExpenseType.objects.all().order_by("exp_source")
            # pass it to context
            context = {
                "cat_list": mypaginator(request, db_query),
                "form": form,
                "cancel_url": cancel,
                "action": action,
            }
            return render(request, "expense/expenseCat.html", context)
    else:
        action = "Update"
        expense_cat_item = ExpenseType.objects.get(pk=expense_cat_id)
        form = expenseCatForm(request.POST or None, instance=expense_cat_item)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect("expenseCat")
        else:
            # Get data from the database
            db_query = ExpenseType.objects.all().order_by("exp_source")
            # pass it to context
            context = {
                "cat_list": mypaginator(request, db_query),
                "form": form,
                "cancel_url": cancel,
                "action": action,
            }
            return render(request, "expense/expenseCat.html", context)


def delete_expense_cat(request, expense_cat_id):
    expense_cat_item = ExpenseType.objects.get(pk=expense_cat_id)
    context = {
        "object_to_delete": expense_cat_item,
        "cancel_url": "expenseCat",
        "item_group": "list of expense categories",
    }
    if request.method == "GET":
        return render(request, "delete.html", context)
    if request.method == "POST":
        expense_cat_item.delete()
        messages.success(
            request, f"{expense_cat_item.expense_source} has been deleted successfully"
        )
        return redirect("expenseCat")
