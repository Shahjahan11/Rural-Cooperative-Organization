from django.urls import path
from .import views


urlpatterns = [
     path('',views.INVEST, name="InvesT"),
     path('edit_invest/<int:invest_id>/', views.edit_invest, name='edit_invest'),
     path('delete_invest/<int:invest_id>/', views.delete_invest, name='delete_invest'),     
]
