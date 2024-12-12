from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from .models import User

admin.site.unregister(Group)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ['id', 'username', 'email', 'full_name', 'is_active']
    list_display_links = ['id', 'username', 'email', 'full_name']
    list_filter = ['is_staff', 'is_superuser', 'is_active']
    search_fields = ['email', 'username', 'full_name']
    fieldsets = [
        [
            "User's data",
            {
                "fields": [
                    "avatar",
                    "username",
                    "email",
                    "full_name",
                    "date_joined",
                    "last_login",
                ]
            }
        ],
        [
            "Extra",
            {
                "fields": ["is_staff", "is_superuser", "is_active"]
            }
        ]
    ]
    readonly_fields = ["date_joined", "last_login"]
    
