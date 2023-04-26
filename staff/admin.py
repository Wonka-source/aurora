from django.contrib import admin
from .models import TeamMember


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):

    fields = ('user', 'position', 'photo', 'bio')

    list_display = ('user', 'position')

    ordering = ('date_registered',)
