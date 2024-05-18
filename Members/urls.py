#urls.py
# from django.urls import path
# from .import views

# urlpatterns = [
#     path('',views.MEMBERS, name="MemberS")
# ]

from django.urls import path
from .views import MEMBERS

urlpatterns = [
    path('members/', MEMBERS, name='MemberS'),
    # Add other URLs as needed
]
