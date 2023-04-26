from django.contrib import admin
from .models import WatchRepair


@admin.register(WatchRepair)
class WatchRepairAdmin(admin.ModelAdmin):

    readonly_fields = ('token', 'timestamp','user_profile', 'quartz', 
                        'mechanical', 'chronograph')

    fields = ('token', 'timestamp', 'status', 'priority', 'user_profile', 'full_name', 'email',
            'phone_number', 'quartz', 'mechanical', 'chronograph', 'description', 'staff_notes')

    list_display = ('full_name', 'status', 'email', 'timestamp', 'priority')

    search_fields = ('full_name', 'email', 'description', 'status', 'priority')
    
    ordering = ('-timestamp',)
