from django.contrib import admin
from .models import TeamMember
from django import forms
from django.contrib.auth.models import User


class TeamMemberAdmin(admin.ModelAdmin):
    model = TeamMember
    readonly_fields = ('date_registered',)
    fields = ('user', 'date_registered', 'name', 'position',
              'phone_number', 'photo', 'bio')
    list_display = ('user', 'name', 'position', 'date_registered')
    ordering = ('date_registered',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            kwargs["queryset"] = User.objects.filter(is_staff=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(TeamMember, TeamMemberAdmin)
