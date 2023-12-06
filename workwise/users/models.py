from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Person(AbstractUser):
    is_employer = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)

    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(max_length=200, unique=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
 

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = "Users"
        verbose_name = "User"
        ordering = ['username'] 







    
   