from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def FONTPAGE(request):
    return  render(request,'Fontpage/Fontpage.html')