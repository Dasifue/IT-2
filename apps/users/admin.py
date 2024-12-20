from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import User

admin.site.unregister(Group)

@admin.register(User)
class AdminSiteUser(UserAdmin):
    list_display = ['id', 'username', 'email', 'full_name']
    list_display_links = ['id', 'username', 'email', 'full_name']
    list_filter = ['is_staff', 'is_superuser', 'is_active']
    search_fields = ['username', 'email', 'full_name']
    fieldsets = [
        [
            "Данные пользователя",
            {
                'fields': [
                    'avatar',
                    'email',
                    'username',
                    'full_name',
                    'date_joined',
                    'last_login',
                    'is_staff',
                    'is_superuser',
                    'is_active'
                ]
            }
        ]
    ]
    readonly_fields = ['date_joined', 'last_login']
