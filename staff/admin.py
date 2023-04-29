from django.contrib import admin
from .models import TeamMember
from django import forms
from django.contrib.auth.models import User


class TeamMemberAdmin(admin.ModelAdmin):
    model = TeamMember
    readonly_fields = ('date_registered',)
    fields = ('user', 'date_registered', 'position',
              'phone_number', 'photo', 'bio')
    list_display = ('user', 'position', 'date_registered')
    ordering = ('date_registered',)

# https://docs.djangoproject.com/en/4.2/ref/contrib/admin/#:~:text=on%20the%20user%3A-,class%20MyModelAdmin(admin.ModelAdmin)%3A,-def%20formfield_for_foreignkey(

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            kwargs["queryset"] = User.objects.filter(is_staff=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(TeamMember, TeamMemberAdmin)
