from django.contrib import admin
from .models import Quiz
# Register your models here.


class QuizAdmin(admin.ModelAdmin):

    ordering = ('-created_at', )


admin.site.register(Quiz, QuizAdmin)
