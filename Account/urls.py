#urls.py
from django.urls import path
from .import views

urlpatterns = [
    path('2018',views.ACCOUNT2018, name="AccounT2018"),
    path('2019',views.ACCOUNT2019, name="AccounT2019"),
    path('2020',views.ACCOUNT2020, name="AccounT2020"),
    path('2021',views.ACCOUNT2021, name="AccounT2021"),
    path('2022/',views.ACCOUNT2022, name="AccounT2022"),
    path('save_payment/', views.save_payment, name='save_payment'),
    path('2023/', views.ACCOUNT2023, name='account2023'),

]




