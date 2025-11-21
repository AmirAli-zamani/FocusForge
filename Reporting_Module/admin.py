from django.contrib import admin
from .models import DailyReport

@admin.register(DailyReport)
class DailyReportAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "date", "tasks_completed", "pomodoros_completed", "productivity_score")
    list_filter = ("date", "user")
    search_fields = ("user__username",)
    ordering = ("-date",)
