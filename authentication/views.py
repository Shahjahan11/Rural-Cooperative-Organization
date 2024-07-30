from django.shortcuts import render, redirect
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import Group

@login_required(login_url='register')
@csrf_exempt
def home_page(request):
    context = {'user': request.user}
    return render(request, 'About/About.html', context)

def registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        error_message = None

        if User.objects.filter(username=username).exists():
            error_message = 'Username already taken'
        elif User.objects.filter(email=email).exists():
            error_message = 'Email already registered'
        
        if error_message:
            return render(request, 'authentication/home.html', {'error': error_message})

        user = User.objects.create_user(username, email, password)
        group = Group.objects.get(name='member')
        print('Got griup',group)
        user.groups.add(group)
        return redirect('home')

    return render(request, 'authentication/home.html')

def LoginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['user'] = username
            return redirect('home')

    return render(request, 'authentication/home.html')
        
def logoutView(request):
    logout(request)
    request.session.clear()
    return redirect('login')