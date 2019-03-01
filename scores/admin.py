from django.contrib import admin
from .models import Score
# Register your models here.


class ScoreAdmin(admin.ModelAdmin):
    list_display = ('quiz', 'team')


admin.site.register(Score, ScoreAdmin)
