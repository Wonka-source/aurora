from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.


class CustomerProfile(models.Model):

    username = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)    
    city = models.Charfield(max_length=80)
    post_code = models.CharField(max_length=25)

    def __str__(self):
        return self.username.username


class StaffProfile(models.Model):

    username = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    admin_permissions = models.BooleanField(default=False)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.username.username