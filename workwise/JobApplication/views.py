from django.shortcuts import render

from .models import JobApplication
from .serializers import JobApplicationSerializer
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser



class JobApplicationViewSet(viewsets.ModelViewSet):
   
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    parser_classes = (MultiPartParser, FormParser)

    #permission_classes = [permissions.IsAuthenticated]


