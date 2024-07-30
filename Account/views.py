# views.py
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt  
from .models import Payment

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
members = ['Shahjahan', 'Kader-1', 'Kader-2', 'Rony', 'Mahibul', 'Shahalom', 'Yousuf', 'Jamal-1', 'Jamal-2', 'Topu',
               'Nizam', 'Tamjid-1', 'Tamjid-2', 'Tawsif', 'Mizan', 'Sayed', 'Al-amin', 'Rafe']

def save_payment(request):
    if request.method == 'POST':
        year = request.POST['year']
        member = request.POST['member']
        month = request.POST['month']
        value = int(request.POST['value'])
        existing_record = Payment.objects.filter(year=year, member=member, month=month).exists()

        if existing_record:
            existing_payment = Payment.objects.get(year=year, member=member, month=month)
            existing_payment.value = value
            existing_payment.save()
        else:
            new_record = Payment(year=year, member=member, month=month, value=value)
            new_record.save()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def ACCOUNT2023(request):
    
    payments = Payment.objects.all()

    dic={}
    for i in payments:
        key=str(i.year)+i.member+i.month
        dic.update({key:i.value})   

    print(dic) 
    data = {'months': months, 'members': members, 'payments': dic}
    return render(request, 'Account/Account2023.html', data)


def ACCOUNT2022(request):
    payments = Payment.objects.all()

    dic={}
    for i in payments:
        key=str(i.year)+i.member+i.month
        dic.update({key:i.value})   

    print(dic) 
    data = {'months': months, 'members': members, 'payments': dic}
    return render(request, 'Account/Account2022.html', data)


def ACCOUNT2021(request):
    payments = Payment.objects.all()

    dic={}
    for i in payments:
        key=str(i.year)+i.member+i.month
        dic.update({key:i.value})   

    print(dic) 
    data = {'months': months, 'members': members, 'payments': dic}
    return render(request, 'Account/Account2021.html', data)

def ACCOUNT2020(request):
    payments = Payment.objects.all()

    dic={}
    for i in payments:
        key=str(i.year)+i.member+i.month
        dic.update({key:i.value})   

    print(dic) 
    data = {'months': months, 'members': members, 'payments': dic}
    return render(request, 'Account/Account2020.html', data)

def ACCOUNT2019(request):
    payments = Payment.objects.all()

    dic={}
    for i in payments:
        key=str(i.year)+i.member+i.month
        dic.update({key:i.value})   

    print(dic) 
    data = {'months': months, 'members': members, 'payments': dic}
    return render(request, 'Account/Account2019.html', data)

def ACCOUNT2018(request):
    payments = Payment.objects.all()

    dic={}
    for i in payments:
        key=str(i.year)+i.member+i.month
        dic.update({key:i.value})   

    print(dic) 
    data = {'months': months, 'members': members, 'payments': dic}
    return render(request, 'Account/Account2018.html', data)





