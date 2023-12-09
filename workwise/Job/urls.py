from .views import *
from django.urls import path
from django.urls import include, re_path
from django.contrib import admin


urlpatterns = [
    re_path('createJob', createJob),
    re_path('jobs' , GetJobs), 
    path('deleteJob/<int:Job_id>',deleteJob),
    path('job/<int:job_id>/', getJobById),
    path('updateJob/<int:job_id>',updateJob)
]