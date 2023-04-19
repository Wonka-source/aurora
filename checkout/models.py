from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.conf import settings
import datetime
import uuid
from shop.models import Product

"""
models based on Code Institute boutique ado project
"""
DELIVERY_METHOD = ((0, "Standard"), (1, "Express"))


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    order_number = models.CharField(max_length=64, null=False, editable=False)
    order_date = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    shipping_address1 = models.CharField(max_length=89, null=False, blank=False)
    shipping_address2 = models.CharField(max_length=89, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    delivery_method = models.IntegerField(choices=DELIVERY_METHOD, default=0)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    order_paid = models.BooleanField(default=False)
    fulfilled = models.BooleanField(default=False)

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return str(uuid.uuid4())

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-order_date']

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.product.name} on order {self.order.order_number}'
