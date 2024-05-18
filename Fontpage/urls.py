from django.urls import path
from .import views

urlpatterns = [
    path('',views.FONTPAGE, name="FontpagE")
]
