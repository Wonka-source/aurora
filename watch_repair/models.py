import uuid

from django.db import models
from profiles.models import UserProfile


class WatchRepair(models.Model):

    """
    A model to represent watch repair enquires
    """

    STATUS = ((0, "New"), (1, "In Progress"), (2, "Complected"))
    PRIORITY = ((0, "Low"), (1, "Medium"), (2, "High"))

    timestamp = models.DateTimeField(auto_now_add=True)
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    quartz = models.BooleanField(default=False)
    mechanical = models.BooleanField(default=False)
    chronograph = models.BooleanField(default=False)
    other = models.BooleanField(default=False)
    description = models.TextField()
    staff_notes = models.TextField(default='')
    status = models.IntegerField(choices=STATUS, default=0)
    priority = models.IntegerField(choices=PRIORITY, default=1)

    def __str__(self):
        return f"{self.full_name} ({self.token})"

    class Meta:
        verbose_name_plural = "Watch Repairs"
        ordering = ["-timestamp"]
