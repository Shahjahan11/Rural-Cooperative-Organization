# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ExpenseForm
from .models import Expense
from django.http import JsonResponse
from django.http import HttpResponseBadRequest


def EXPENSE(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('ExpensE')  # Redirect to the expense page after submission
    else:
        form = ExpenseForm()

    expenses = Expense.objects.all()

    return render(request, 'Expense/Expense.html', {'form': form, 'expenses': expenses})



def edit_expense(request, expense_id):
    
    try:
        expense = Expense.objects.get(pk=expense_id)
        expense.person = request.POST.get('productCode')
        expense.description = request.POST.get('product')
        expense.date = request.POST.get('qty')
        expense.amount = request.POST.get('perPrice')
        expense.save()
        return JsonResponse({'status': 'success', 'message': 'Expense updated successfully'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': f'Error: {str(e)}'})



def delete_expense(request, expense_id):
    try:
        expense = Expense.objects.get(pk=expense_id)
        print(f"Deleting expense: {expense}")
        expense.delete()
        return JsonResponse({'status': 'success', 'message': 'Expense deleted successfully'})
    except Exception as e:
        print(f"Error deleting expense: {e}")
        return JsonResponse({'status': 'error', 'message': str(e)})
