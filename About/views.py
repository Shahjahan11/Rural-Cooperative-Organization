from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def ABOUT(request):
    return  render(request,'About/About.html')

