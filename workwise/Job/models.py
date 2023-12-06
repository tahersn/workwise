from django.db import models
from users.models import Person


# Create your models here.
class Job(models.Model):
    employer = models.ForeignKey(Person, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=200)
    job_description = models.TextField()
    job_location = models.CharField(max_length=200)
    job_type = models.CharField(max_length=200)
    job_category = models.CharField(max_length=200)
    job_company = models.CharField(max_length=200)
    job_experience = models.CharField(max_length=200)
    job_salary = models.CharField(max_length=200)
    job_qualification = models.CharField(max_length=200)
    job_posted_on = models.DateTimeField(auto_now_add=True)
    job_updated_on = models.DateTimeField(auto_now=True)
    job_status = models.BooleanField(default=True)

    def __str__(self):
        return self.job_title

    class Meta:
        verbose_name_plural = "Jobs"
        verbose_name = "Job"
        ordering = ['job_posted_on']

