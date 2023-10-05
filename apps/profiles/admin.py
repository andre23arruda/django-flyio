from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

class ProfileInline(admin.StackedInline):
    can_delete = False
    max_num = 1
    model = Profile
    verbose_name = 'Profile'
    verbose_name_plural = 'Profile'

class UserRegister(UserAdmin):
    inlines = [ProfileInline]
    list_filter = ['is_staff', 'is_active']
    search_fields = ['email', 'username']

    class Media:
        css = {'all': ('css/stacked-inline.css',)}

admin.site.unregister(User)
admin.site.register(User, UserRegister)