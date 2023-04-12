from django.db import models

# Create your models here.


class Order(models.Model):

    STATUS = (
        ('received', 'Order Received'),
        ('processing', 'Processing'),
        ('dispatched', 'Dispatched'),
        ('pending', 'Status Pending'),
        ('canceled', 'Canceled'),
        ('refunded', 'Refunded'),
    )