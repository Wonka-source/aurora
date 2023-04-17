from django.db import models
from cloudinary.models import CloudinaryField


class Category(models.Model):
    name = models.CharField(max_length=255)
    friendly_name = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Brand(models.Model):
    name = models.CharField(max_length=255)
    friendly_name = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


STOCK = ((0, "In stock"), (1, "Running low"), (2, "Out of stock"))


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL, related_name='products')
    brand = models.ForeignKey(Brand, null=True, blank=True, on_delete=models.SET_NULL, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    has_color_option = models.BooleanField(default=False, null=True, blank=True)
    image = CloudinaryField('image', null=True, blank=True, default='placeholder')
    stock = models.IntegerField(choices=STOCK, default=0)
    type = models.CharField(max_length=50, choices=(
        ('watch', 'Watch'),
        ('strap', 'Watch Strap'),
        ('tool', 'Tool'),
    ))

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name
