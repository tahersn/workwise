from django.shortcuts import render
from .models import Job
from .Forms import JobForm
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


# Create your views here.
@api_view(['POST'])
def createJob(request):
    if request.method == 'POST':
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            # If employer_id is not provided in the request data, you can set it here.
            # This assumes that employer_id is a required field.
            serializer.save(employer_id=2)
            return Response({'message': 'Job created successfully'}, status=201)
        else:
            return Response({'error': 'Invalid data'}, status=400)

    return Response({'error': 'Method not allowed'}, status=405)