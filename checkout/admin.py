from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'order_date', 'delivery_cost', 'order_total', 'grand_total', 'original_cart', 'stripe_pid')

    fields = ('order_number', 'order_date', 'full_name', 'user', 'email', 'phone_number', 'shipping_address1', 'shipping_address2', 'delivery_method', 'delivery_cost', 'order_total', 'grand_total', 'fulfilled', 'original_cart', 'stripe_pid')

    list_display = ('order_number', 'order_date', 'full_name',
    'delivery_cost', 'grand_total', 'fulfilled')

    ordering = ('-order_date',)


admin.site.register(Order, OrderAdmin)
