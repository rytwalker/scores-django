from django.contrib import admin
from .models import Score


class ScoreAdmin(admin.ModelAdmin):
    list_display = ('quiz', 'team', 'total_points_scored')


admin.site.register(Score, ScoreAdmin)
