from rest_framework import serializers
from .models import JobApplication,ApplicationStatusEnum

class JobApplicationSerializer(serializers.ModelSerializer):
    application_status = serializers.ChoiceField(choices=[status.value for status in ApplicationStatusEnum])
    class Meta:
        model = JobApplication
        fields = '__all__'