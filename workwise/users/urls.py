
# users/urls.py

from django.urls import path
from .views import sign_up,sign_in

urlpatterns = [
    path('sign_up/', sign_up, name='sign_up'),
    path('sign_in/', sign_in, name='sign_in'),
    # Add other URLs as needed
]
