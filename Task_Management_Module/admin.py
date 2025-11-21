from django.contrib import admin
from .models import Task, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "owner", "status", "priority", "deadline")
    list_filter = ("status", "priority", "category")
    search_fields = ("title", "description")
    autocomplete_fields = ("owner", "category")
