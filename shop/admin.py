from django.contrib import admin
from .models import Product, Brand, Category

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (        
        'name',
        'brand',
        'price',
        'image',
    )

    ordering = ['brand__name', 'name']


class BrandAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Category, CategoryAdmin)
