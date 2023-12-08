from django.shortcuts import render
from .models import Job
from .Forms import JobForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import JobSerializer




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

# @api_view(['GET'])
def GetJobs (request):
    jobs = Job.objects.all()
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)

def getJobById (Job_id):
    try:
        job = Job.objects.get(pk=Job_id)
        return job
    except Job.DoesNotExist:
        return Response({'Job Not Found'})

def deleteJob (Job_id):
    try:
        res = Job.objects.delete(pk=Job_id) 
        return Response({'job deleted successfully'})
    except Job.DoesNotExist:
        return Response({'No Job Found'})       

def updateJob(request, job_id):
    try:
        job = Job.objects.get(pk=job_id)

        if request.method == 'POST':
            serializer = JobSerializer(instance=job, data=request.data)

            if serializer.is_valid():
                # If employer_id is not provided in the request data, you can set it here.
                # This assumes that employer_id is a required field.
                serializer.save(employer_id=2)
                return Response({'message': 'Job updated successfully'}, status=200)
            else:
                return Response({'error': 'Verify your data'}, status=400)

    except Job.DoesNotExist:
        return Response({'error': 'Job not found'}, status=404)

    return Response({'error': 'Invalid request method'}, status=405)


