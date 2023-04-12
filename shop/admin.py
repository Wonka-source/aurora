from django.contrib import admin
from .models import Watch, Brand

# Register your models here.


class WatchAdmin(admin.ModelAdmin):
    list_display = (        
        'name',
        'brand',
        'sku',
        'price',
        'image',
    )

    ordering = ['brand__name', 'name']


class BrandAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Watch, WatchAdmin)
admin.site.register(Brand, BrandAdmin)


