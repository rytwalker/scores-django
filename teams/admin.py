from django.contrib import admin
from .models import Team


class TeamAdmin(admin.ModelAdmin):
    search_fields = ('team_name',)
    ordering = ('team_name',)


admin.site.register(Team, TeamAdmin)
