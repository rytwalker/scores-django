from django.contrib import admin
from .models import Score


class ScoreAdmin(admin.ModelAdmin):
    list_display = ('quiz', 'team', 'total_points_scored')
    list_filter = ('quiz',)
    search_fields = ('team__team_name',)
    ordering = ('-quiz__created_at', '-total_points_scored')


admin.site.register(Score, ScoreAdmin)
