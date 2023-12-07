from .views import *
from django.urls import path
from django.urls import include, re_path
from django.contrib import admin

urlpatterns = [
    re_path('createJob', createJob),
]