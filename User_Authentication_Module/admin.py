from django.contrib import admin
from .models import CustomUser

# ----------------------------
# CustomUser Admin
# ----------------------------
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    # Columns to display in admin list view
    list_display = ("username", "email", "bio", "is_staff", "is_active")
    
    # Enable search by username and email
    search_fields = ("username", "email")
    
    # Default ordering in list view
    ordering = ("username",)
    
    # Optional: group fields in fieldsets for cleaner editing
    fieldsets = (
        ("Login Info", {"fields": ("username", "password")}),
        ("Personal Info", {"fields": ("email", "bio", "avatar")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
        ("Important Dates", {"fields": ("last_login", "date_joined")}),
    )
