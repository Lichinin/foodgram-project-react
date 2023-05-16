from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import FoodgramUser, Follow


@admin.register(FoodgramUser)
class FoodgramUser(UserAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name')
    list_filter = ('email', 'username')


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('user', 'author')
