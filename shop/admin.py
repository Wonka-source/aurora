from django.contrib import admin
from .models import Product, Brand, Watch, Category, WatchStrap

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (        
        'name',
        'brand',
        'price',
        'image',
    )

    ordering = ['brand__name', 'name']


class WatchAdmin(admin.ModelAdmin):
    list_display = (        
        'mechanism_type',
        'color',
        'material',        
    )


class BrandAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class WatchStrapAdmin(admin.ModelAdmin):
    list_display = (
        'strap_type',
        'color',
        'material',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(WatchStrap, WatchStrapAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Watch, WatchAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Category, CategoryAdmin)
