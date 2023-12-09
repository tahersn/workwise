from django.db import models
from Job.models import Job
from users.models import Person
from enum import Enum

class ApplicationStatusEnum(Enum):
    PENDING = 'Pending'
    ACCEPTED = 'Accepted'
    REJECTED = 'Rejected'

# Create your models here.
class JobApplication (models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    employee = models.ForeignKey(Person, on_delete=models.CASCADE)
    CV = models.FileField(upload_to='jobApplication/cvs', blank=True, null=True)
    Cover_letter = models.TextField()
    application_date = models.DateTimeField(auto_now_add=True)
    application_status = models.CharField(
        max_length=20,
        choices=[(status.name, status.value) for status in ApplicationStatusEnum],
        default=ApplicationStatusEnum.PENDING.name,
    ) 

    def __str__(self):
        return self.job.job_title + " - " + self.employee.user.username

    class Meta:
        verbose_name_plural = "Job Applications"
        verbose_name = "Job Application"
        ordering = ['-application_date']
