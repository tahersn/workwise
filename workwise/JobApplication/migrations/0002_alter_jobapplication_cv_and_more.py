# Generated by Django 4.1.5 on 2023-12-09 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobApplication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='CV',
            field=models.FileField(blank=True, null=True, upload_to='job_application/cvs'),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='application_status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('ACCEPTED', 'Accepted'), ('REJECTED', 'Rejected')], default='PENDING', max_length=20),
        ),
    ]
