from .views import *
from django.urls import path
from django.urls import include, re_path
from django.contrib import admin

urlpatterns = [
    re_path('createJob', createJob),
    re_path('jobs' , GetJobs), 
    re_path('deleteJob',deleteJob),
    re_path('job',getJobById),
    re_path('updateJob',updateJob)
]