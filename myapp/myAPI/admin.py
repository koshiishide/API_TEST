from django.contrib import admin

from .models import User


@admin.register(User) #デコレーター
class UserAdmin(admin.ModelAdmin):
    pass

