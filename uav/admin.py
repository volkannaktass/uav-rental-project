from django.contrib import admin
from .models import Uav 
# Register your models here.

### To show and control model in the admin page, registered the model.
@admin.register(Uav)
class UavAdmin(admin.ModelAdmin):
    
    list_display = ["title","author","created_date"]
    list_display_links = ["title","created_date"]
    search_fields = ["title"]
    list_filter = ["created_date"]
    class Meta:
        model = Uav

