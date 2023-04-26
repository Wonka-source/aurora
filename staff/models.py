from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


class TeamMember (models.Model):
    """
    A model for staff members to be displayed on the about page.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='team_member')
    position = models.CharField(max_length=255)
    bio = models.TextField(blank=True)
    photo = CloudinaryField('image', default='staff_placeholder')
    date_registered = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Team Members"
        ordering = ["date_registered"]

    def __str__(self):
        return self.user.get_full_name()
