from django.db import models
from django.contrib.auth.models import User


class CustomerProfile(models.Model):

    """
    A model representing a customer profile, linked to a user account.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=80)
    post_code = models.CharField(max_length=25)

    def __str__(self):
        return self.user.username
