from django.db import models

# Create your models here.


class ShopWatches(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    price = DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    mechanism_type = models.CharField(max_length=50, choices=(
        ('quartz', 'Quartz'),
        ('mechanical', 'Mechanical'),
        ('automatic', 'Automatic'),
        ('kinetic', 'Kinetic'),
        ('digital', 'Digital'),
        ('solar', 'Solar-powered'),
        ('smart', 'Smart'),
        ('other', 'Other'),
    ))
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name
