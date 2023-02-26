from django.contrib import admin
from . import views
from django.urls import path,include

app_name = "uav"
urlpatterns = [
  
    path('dashboard/',views.dashboard,name = "dashboard"),
    path('register-uav/',views.registerUav,name = "register-uav"),
    path('list/',views.showUav,name = "uavs"),
    #path('uav/<int:id>',views.detail,name = "detail"),
    path('update/<int:id>',views.updateUav,name = "update"),
    path('delete/<int:id>',views.deleteUav,name = "delete"),
    #path('',views.uav,name = "uav"),

    #path('uavtable/<int:id>',views.showUav,name = "uavtable"),
  
]
