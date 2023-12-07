from django.contrib import admin
from django.utils.safestring import mark_safe
from django.contrib import messages

from .models import Job

# Register your models here.

class JobAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'job_type', 'job_category', 'job_location', 'job_salary', 'job_status', 'job_posted_on', 'job_updated_on')
    list_editable = ('job_status',)
    list_filter = ('job_type', 'job_category', 'job_location', 'job_status', 'job_posted_on', 'job_updated_on')
    search_fields = ('job_title', 'job_description', 'job_company')
    readonly_fields = ('job_posted_on', 'job_updated_on')

    fieldsets = (
        ('Job Details', {
            'fields': ('job_title', 'job_description', 'job_company', 'job_location', 'job_type', 'job_category', 'job_experience', 'job_salary', 'job_qualification', 'job_status')
        }),
        ('Job Dates', {
            'fields': ('job_posted_on', 'job_updated_on')
        }),
    )
    

admin.site.register(Job, JobAdmin)    