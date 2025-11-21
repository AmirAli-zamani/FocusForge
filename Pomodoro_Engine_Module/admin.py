from django.contrib import admin
from .models import PomodoroSession

@admin.register(PomodoroSession)
class PomodoroSessionAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "task", "start_time", "end_time", "is_completed", "duration_minutes")
    list_filter = ("is_completed", "duration_minutes")
    search_fields = ("user__username", "task__title")
    ordering = ("-start_time",)
    autocomplete_fields = ("user", "task")
