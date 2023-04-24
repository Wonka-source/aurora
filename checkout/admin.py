from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date', 'delivery_cost', 'user_profile',
                       'order_total', 'grand_total', 'original_cart', 'stripe_pid')

    fields = ('order_number', 'date', 'full_name', 'user_profile', 'email', 'phone_number', 'shipping_address1', 'shipping_address2',
              'delivery_method', 'delivery_cost', 'order_total', 'grand_total', 'fulfilled', 'original_cart', 'stripe_pid')

    list_display = ('order_number', 'date', 'full_name',
                    'delivery_cost', 'grand_total', 'fulfilled')

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
