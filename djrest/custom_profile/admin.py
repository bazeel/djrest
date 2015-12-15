from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import UserCustomProfile


class UserCustomProfileInline(admin.StackedInline):
    model = UserCustomProfile


class CustomUserAdmin(UserAdmin):
    inlines = [UserCustomProfileInline]


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
