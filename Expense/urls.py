from django.urls import path
from .import views


urlpatterns = [
     path('',views.EXPENSE, name="ExpensE"),
     path('edit_expense/<int:expense_id>/', views.edit_expense, name='edit_expense'),
     path('delete_expense/<int:expense_id>/', views.delete_expense, name='delete_expense'),     
]
