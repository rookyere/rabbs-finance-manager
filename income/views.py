from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Income, IncomeType
from .forms import IncomeCatForm, IncomeItemForm
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator

# Create your views here.
def mypaginator(request, db_query):
    p = Paginator(db_query, 10)
    page = request.GET.get("page")
    cat_list = p.get_page(page)
    return cat_list


def income_item(request, income_item_id=None):
    cancel = "income"

    if income_item_id is None:
        action = "Add"
        # Create a new income category
        if request.method == "POST":
            form = IncomeItemForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Income item has been addded successfully")
                return redirect("income")
            else:
                # Initialize an emoty form for Get requests
                form = IncomeItemForm(request.POST)
                # Get data from the database
                db_query = Income.objects.all().order_by("-income_date",'-income_date_time')
                # pass it to context
                context = {
                    "income_list": mypaginator(request, db_query),
                    "form": form,
                    "action": action,
                    "cancel_url": cancel,
                }

                messages.error(request, "Invalid form submission.")
                # messages.error(request, form.errors)
                return render(request, "income/income.html", context)
        else:
            # Initialize an emoty form for Get requests
            form = IncomeItemForm()
            # Get data from the database
            db_query = Income.objects.all().order_by("-income_date",'-income_date_time')
            # pass it to context
            context = {
                "income_list": mypaginator(request, db_query),
                "form": form,
                "action": action,
                "cancel_url": cancel,
            }
            return render(request, "income/income.html", context)
    else:
        action = "Update"
        income_list_item = Income.objects.get(pk=income_item_id)
        form = IncomeItemForm(request.POST or None, instance=income_list_item)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect("income")
            else:
                # Initialize an emoty form for Get requests
                form = IncomeItemForm(request.POST)
                # Get data from the database
                db_query = Income.objects.all().order_by("-income_date",'-income_date_time')
                # pass it to context
                context = {
                    "income_list": mypaginator(request, db_query),
                    "form": form,
                    "action": action,
                    "cancel_url": cancel,
                }

                messages.error(request, "Invalid form submission.")
                # messages.error(request, form.errors)
                return render(request, "income/income.html", context)
        else:
            # Get data from the database
            db_query = Income.objects.all().order_by("-income_date",'-income_date_time')
            # pass it to context
            context = {
                "income_list": mypaginator(request, db_query),
                "form": form,
                "action": action,
                "cancel_url": cancel,
            }
            return render(request, "income/income.html", context)


def delete_income_item(request, income_item_id):
    income_item = Income.objects.get(pk=income_item_id)
    context = {
        "object_to_delete": income_item,
        "cancel_url": "income",
        "item_group": "list of income",
    }
    if request.method == "GET":
        return render(request, "delete.html", context)
    if request.method == "POST":
        income_item.delete()
        messages.success(
            request, f"{income_item.description} has been deleted successfully"
        )
        return redirect("income")


def income_cat(request, income_cat_id=None):
    cancel = "incomeCat"

    if income_cat_id is None:
        # Create a new income category
        action = "Add"
        if request.method == "POST":
            form = IncomeCatForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(
                    request, f"Income Category has been created successfully"
                )
                return redirect("incomeCat")
            else:
                print(form.errors)
                messages.error(request, "Invalid form submission.")
                messages.error(request, form.errors)
        else:
            # Initialize an emoty form for Get requests
            form = IncomeCatForm()
            # Get data from the database
            db_query = IncomeType.objects.all().order_by('-income_source')
            # pass it to context
            context = {
                "cat_list": mypaginator(request, db_query),
                "form": form,
                "action": action,
                "cancel_url": cancel,
            }
            return render(request, "income/incomeCat.html", context)
    else:
        action = "Update"
        income_cat_item = IncomeType.objects.get(pk=income_cat_id)
        form = IncomeCatForm(request.POST or None, instance=income_cat_item)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect("incomeCat")
        else:
            # Get data from the database
            db_query = IncomeType.objects.all().order_by('-income_source')
            # pass it to context
            context = {
                "cat_list": mypaginator(request, db_query),
                "form": form,
                "action": action,
                "cancel_url": cancel,
            }
            return render(request, "income/incomeCat.html", context)


def delete_income_cat(request, income_cat_id):
    income_cat_item = IncomeType.objects.get(pk=income_cat_id)
    context = {
        "object_to_delete": income_cat_item,
        "cancel_url": "incomeCat",
        "item_group": "list of income categories",
    }
    if request.method == "GET":
        return render(request, "delete.html", context)
    if request.method == "POST":
        income_cat_item.delete()
        messages.success(
            request, f"{income_cat_item.income_source} has been deleted successfully"
        )
        return redirect("incomeCat")
