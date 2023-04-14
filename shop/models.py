from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


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
    image = CloudinaryField('image', null=True, blank=True)
    stock = models.IntegerField(choices=STOCK, default=0)

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name


class Watch(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True)
    mechanism_type = models.CharField(max_length=50, choices=(
        ('quartz', 'Quartz'),
        ('mechanical', 'Mechanical'),
        ('automatic', 'Automatic'),
        ('kinetic', 'Kinetic'),
        ('digital', 'Digital'),
    ))
    color = models.CharField(max_length=50, null=True, blank=True)
    material = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Watches'

    def __str__(self):
        return self.product.name


class WatchStrap(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True)
    strap_type = models.CharField(max_length=50, choices=(
        ('nato', 'Nato Strap'),
        ('zulu', 'Zulu Strap'),
        ('perlon', 'Perlon Strap'),
        ('leather', 'Leather Strap'),
        ('rubber', 'Rubber Strap'),
        ('silicone', 'Silicone Strap'),
        ('metal', 'Metal Bracelet'),
        ('leather', 'Leather Strap'),
    ))
    color = models.CharField(max_length=50, null=True, blank=True)
    material = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Watch Straps'

    def __str__(self):
        return self.product.name
