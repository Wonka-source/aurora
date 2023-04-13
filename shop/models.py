from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=255)
    friendly_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


STOCK = ((0, "Out of stock "), (1, "In stock"), (2, "Running low"))


class Watch(models.Model):
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=255, null=True, blank=True)
    brand = models.ForeignKey(Brand, null=True, blank=True, on_delete=models.SET_NULL, related_name='watches')
    price = models.DecimalField(max_digits=10, decimal_places=2)
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
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = CloudinaryField(blank=True, default='placeholder')
    stock = models.IntegerField(choices=STOCK, default=0)

    class Meta:
        verbose_name_plural = 'Watches'
        ordering = ['brand__name', 'name']

    def __str__(self):
        return self.name




