from django.contrib import admin
from .models import UserProfile




### Register the model to show in the admin panel
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["user","phone_number","gender"]
    list_display_links = ["user","phone_number","gender"]
    search_fields = ["user","phone_number","gender"]
    list_filter = ["user","phone_number","gender"]

admin.site.register(UserProfile,UserProfileAdmin)
