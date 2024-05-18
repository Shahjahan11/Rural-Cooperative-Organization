from django.urls import path
from .import views


urlpatterns = [
     path('',views.INTEREST, name="InteresT"),
     path('edit_interest/<int:interest_id>/', views.edit_interest, name='edit_interest'),
     path('delete_interest/<int:interest_id>/', views.delete_interest, name='delete_interest'),     
]
