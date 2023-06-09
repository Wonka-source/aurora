from django.db import models
from cloudinary.models import CloudinaryField


class Category(models.Model):
    """
    Model representing a product category.
    """
    name = models.CharField(max_length=255)
    friendly_name = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


STOCK = ((0, "In stock"), (1, "Running low"), (2, "Out of stock"))


class Product(models.Model):
    """
    Model representing a product.
    """

    name = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='products'
        )
    brand = models.CharField(max_length=255, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = CloudinaryField(
        'image', null=True, blank=True, default='placeholder')
    stock = models.IntegerField(choices=STOCK, default=0)

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name
