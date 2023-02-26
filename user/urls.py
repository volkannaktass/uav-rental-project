
from django.urls import path,include
from . import views
from .views import ResetPasswordView
from django.contrib.auth import views as auth_views

app_name = "user"
### register, login and logut url and their views to execute new func 
urlpatterns = [
    path('register/',views.register,name = "register"),
    path('login/',views.loginUser,name = "login"),
    path('logout/',views.logoutUser,name = "logout"),
   
]

