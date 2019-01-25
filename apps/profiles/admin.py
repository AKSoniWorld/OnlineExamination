from django.contrib import admin

from .models import (
    Profile
)

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'fullname',
        'join_on',
        'update_on',
        'status',
        'type_of_profile'
    ]
