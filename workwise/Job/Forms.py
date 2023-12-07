
from .models import Job
from django.forms import ModelForm
from django import forms

Status_Choices = (
    "Active", "Active",
    "Closed", "Closed",)

Categ_Choices = (
    "Accounting", "Accounting",
    "Banking", "Banking",
    "Engineering", "Engineering",
    "IT", "IT",
    "Marketing", "Marketing",
    "Sales", "Sales",
    "Teaching", "Teaching",)
Type_Choices = (
    "Full Time", "Full Time",
    "Part Time", "Part Time",
    "Internship", "Internship",
    "Freelance", "Freelance",
    "Temporary", "Temporary",)        

class JobForm(forms.Form):
    employer = 2
    job_title = forms.CharField(max_length=200)
    job_description = forms.CharField(widget=forms.Textarea)
    job_location = forms.CharField(max_length=200)

    job_type = forms.ChoiceField(choices=Type_Choices)
    job_category = forms.ChoiceField(choices=Categ_Choices)
    job_company = forms.CharField(max_length=200)
    job_experience = forms.CharField(max_length=200)
    job_salary = forms.CharField(max_length=200)
    job_qualification = forms.CharField(max_length=200)
    job_posted_on = forms.DateTimeField()
    job_updated_on = forms.DateTimeField()
    job_status = forms.ChoiceField(choices=Status_Choices)




# class JobForm(ModelForm):
#     class Meta:
#         model = Job
#         fields = '__all__'

#         exclude = ['job_posted_on', 'job_updated_on', 'job_status']



