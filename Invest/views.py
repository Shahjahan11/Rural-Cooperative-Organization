# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .forms import InvestForm
from .models import Invest
from django.http import JsonResponse
from django.http import HttpResponseBadRequest


def INVEST(request):
    if request.method == 'POST':
        form = InvestForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('InvesT')  # Redirect to the expense page after submission
    else:
        form = InvestForm()

    invests = Invest.objects.all()

    return  render(request,'Invest/Invest.html', {'form': form, 'invests': invests})


def edit_invest(request, invest_id):
    
    try:
        invest = Invest.objects.get(pk=invest_id)
        invest.person = request.POST.get('productCode')
        invest.description = request.POST.get('product')
        invest.date = request.POST.get('qty')
        invest.amount = request.POST.get('perPrice')
        invest.save()
        return JsonResponse({'status': 'success', 'message': 'Invest updated successfully'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': f'Error: {str(e)}'})



def delete_invest(request, invest_id):
    try:
        invest = Invest.objects.get(pk=invest_id)
        print(f"Deleting invest: {invest}")
        invest.delete()
        return JsonResponse({'status': 'success', 'message': 'Invest deleted successfully'})
    except Exception as e:
        print(f"Error deleting invest: {e}")
        return JsonResponse({'status': 'error', 'message': str(e)})
