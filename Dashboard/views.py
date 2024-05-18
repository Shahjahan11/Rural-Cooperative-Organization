#views.py
from django.http import HttpResponse
from django.shortcuts import render
from Account.models import Payment
from Expense.models import Expense
from Interest.models import Interest
from Invest.models import Invest

# Create your views here.

def DASHBOARD(request):
    tmp = Payment.objects.all()
    sum1 = 0
    sum2 = 0
    sum3 = 0
    sum4 = 0
    sum5 = 0
    for i in tmp:  sum1 += i.value

    tmp2 = Expense.objects.all()
    for i in tmp2:   sum2 += i.amount

    tmp3 = Interest.objects.all()
    for i in tmp3: sum3 += i.amount

    tmp4 = Invest.objects.all()
    for i in tmp4:   sum4 += i.amount


    current_balance = sum1-sum2+sum3-sum4-sum5
    context = {
        'sum1':sum1,
        'sum2':sum2,
        'sum3':sum3,
        'sum4':sum4,
        'sum5':sum5,
        'current_balance':current_balance
    }
    return  render(request,'Dashboard/Dashboard.html',context)
