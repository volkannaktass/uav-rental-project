from django.contrib import admin
from . import views
from django.urls import path,include



### Put the all routes and related views about uav
app_name = "uav"
urlpatterns = [
  
    path('dashboard/',views.dashboard,name = "dashboard"),
    path('register-uav/',views.registerUav,name = "register-uav"),
    path('list/',views.showUav,name = "uavs"),
    path('update/<int:id>',views.updateUav,name = "update"),
    path('delete/<int:id>',views.deleteUav,name = "delete"),
  
]
