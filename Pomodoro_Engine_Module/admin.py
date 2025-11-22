from django.contrib import admin
from .models import PomodoroSession

@admin.register(PomodoroSession)
class PomodoroSessionAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "task", "start_time", "end_time", "status", "duration_minutes")
    list_filter = ("status", "duration_minutes")  # بجای is_completed از status استفاده کن
    search_fields = ("user__username", "task__title")
    ordering = ("-start_time",)
    autocomplete_fields = ("user", "task")
