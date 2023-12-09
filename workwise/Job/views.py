from django.shortcuts import render
from .models import Job
from .Forms import JobForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import JobSerializer
from django.shortcuts import get_object_or_404





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

@api_view(['GET'])
def GetJobs (request):
    jobs = Job.objects.all()
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)

#get one job by id
@api_view(['GET'])
def getJobById(request , job_id):
    job = get_object_or_404(Job , pk=job_id)
    if(request.method == 'GET'):
        serializer = JobSerializer(job)
        return Response(serializer.data)
    else:
        return Response({'error': 'Invalid request method'}, status=405)
    return Response({'error': 'Invalid request method'}, status=405)        
@api_view(['DELETE'])
def deleteJob (self , Job_id):
    try:
        job = get_object_or_404(Job , pk=Job_id) 
        job.delete()
        return Response({'job deleted successfully'})
    except Job.DoesNotExist:
        return Response({'No Job Found'})     

@api_view(['PUT'])
def updateJob(request, job_id):
    try:
        job = get_object_or_404(Job ,  pk=job_id)

        if request.method == 'PUT':
            serializer = JobSerializer(instance=job, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Job updated successfully'}, status=200)
            else:
                return Response({'error': 'Verify your data'}, status=400)
    except Job.DoesNotExist:
        return Response({'error': 'Job not found'}, status=404)

    return Response({'error': 'Invalid request method'}, status=405)


