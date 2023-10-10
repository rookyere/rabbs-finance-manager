from django.shortcuts import render
from expense.models import Expense, ExpenseType
from income.models import Income, IncomeType
from budget.models import BudgetExpense
from django.db.models import Sum
from datetime import datetime
import decimal

# Create your views here.
def to_2_decimal_places(amount):
    return decimal.Decimal(amount).quantize(decimal.Decimal('0.00'))


def dashboard(request):
    this_month = datetime.now().month
    this_year = datetime.now().year


    # Income Statistics
    all_income_data = Income.objects.all()

    this_year_income_data = all_income_data.filter(income_date__year=this_year)
    total_income_this_year = this_year_income_data.aggregate(value=Sum("amount"))
    if total_income_this_year["value"] is None:
        total_income_this_year = 0  
    else:   total_income_this_year = total_income_this_year["value"]

    this_month_income_data = all_income_data.filter(income_date__month=this_month)
    total_income_this_month = this_month_income_data.aggregate(value=Sum("amount"))
    if total_income_this_month["value"] is None:
        total_income_this_month = 0 
    else: total_income_this_month = total_income_this_month["value"]

    # Expense Statistics
    all_expense_data = Expense.objects.all()

    this_year_expense_data = all_expense_data.filter(exp_date__year=this_year)
    total_expense_this_year = this_year_expense_data.aggregate(value=Sum("exp_amount"))
    if total_expense_this_year["value"] is None:
        total_expense_this_year = 0 
    else:  total_expense_this_year = total_expense_this_year["value"]

    this_month_expense_data = all_expense_data.filter(exp_date__month=this_month)
    total_expense_this_month = this_month_expense_data.aggregate(value=Sum("exp_amount"))
    if total_expense_this_month["value"] is None:
        total_expense_this_month = 0  
    else: total_expense_this_month = total_expense_this_month["value"]


    #Budget Statistics
    all_bexpense_data = BudgetExpense.objects.all()

    this_month_bexpense_data = all_bexpense_data.filter(est_expense_date__month=this_month)
    total_bexpense_this_month = this_month_bexpense_data.aggregate(value=Sum("est_amount"))
    if total_bexpense_this_month["value"] is None:
        total_bexpense_this_month = 0  
    else: total_bexpense_this_month = total_bexpense_this_month["value"]



    # Calculate year_income_bal
    year_income_bal = total_income_this_year - total_expense_this_year
 
     # Calculate month_expense_budget_bal
    month_expense_budget_bal = total_income_this_month - total_bexpense_this_month
 
    #calculate month_income_bal
    month_income_bal = total_income_this_month - total_expense_this_month

    #============================================================================
    # cat_amount = this_month_expense_data.values('exp_source__exp_source').annotate(total_cat=Sum('exp_amount'))  
    actual_cat_result_list = this_month_expense_data.values('exp_source__exp_source').annotate(total_cat_amt=Sum('exp_amount'))
    est_cat_result_list = BudgetExpense.objects.values('est_expense_source__exp_source').annotate(total_bexpense_amt=Sum('est_amount'))
    # print(actual_cat_amount_data_dict)
    # result = ExpenseType.objects.values('exp_source').annotate(total_expense=Sum('est_amount')).order_by('exp_source')
    cat_result_list = []
    for cat_item_dict in actual_cat_result_list:
        cat_result_dict = {}
        cat_result_dict['expense_cat'] = cat_item_dict['exp_source__exp_source']
        cat_result_dict['total_cat_amt'] = to_2_decimal_places(cat_item_dict['total_cat_amt'] or 0)

        cat_result_dict['total_bexpense_amt'] = to_2_decimal_places(0)
        
        for est_cat_item_dict in est_cat_result_list:
            if est_cat_item_dict['est_expense_source__exp_source'] == cat_item_dict['exp_source__exp_source']:
                cat_result_dict['total_bexpense_amt'] = to_2_decimal_places(est_cat_item_dict['total_bexpense_amt'])
            
                
        cat_result_dict['variance'] = cat_result_dict['total_bexpense_amt'] - cat_result_dict['total_cat_amt']

        cat_result_list.append(cat_result_dict)
    
    # print(cat_result_list)




    # # print(actual_cat_result_dict)
    # print('==================================================')
    # print(est_cat_result_dict)
    # for item in cat_amount:
    #     print(item['expense_source__expense_source'], ':', item['total_cat'])
    #============================================================================
    
  
    context = {
        "this_year": this_year,
        "this_month": datetime.now().strftime("%B"),
        "total_income_this_year": to_2_decimal_places(total_income_this_year),
        "total_income_this_month": to_2_decimal_places(total_income_this_month),
        "total_expense_this_year": to_2_decimal_places(total_expense_this_year),
        "total_expense_this_month": to_2_decimal_places(total_expense_this_month),
        "year_income_bal": to_2_decimal_places(year_income_bal),
        "month_income_bal": to_2_decimal_places(month_income_bal),
        "total_bexpense_this_month": to_2_decimal_places(total_bexpense_this_month),
        "month_expense_budget_bal": to_2_decimal_places(month_expense_budget_bal),
        "cat_result_list": cat_result_list
    }
    # print("================dddd======================")
 
    # print("AMOUNT:", this_month_expense_amount["value"])
    return render(request, "dashboard.html", context)


def budget_by_expense_cat():
    Expense.objects.aaggregate()
    pass