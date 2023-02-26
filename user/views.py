from django.shortcuts import render,redirect,get_object_or_404
from .forms import (
    RegisterForm,
    LoginForm,
    UserProfileForm
)

from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib.auth import login,authenticate,logout
#from uav.models import Uav
from .models import UserProfile
from django.http import Http404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash





def register(request):
    """ Register """
    
    form = RegisterForm(request.POST or None)
    profile_form = UserProfileForm(request.POST or None)
    if form.is_valid() and profile_form.is_valid():
        first_name = form.cleaned_data.get("first_name")
        last_name = form.cleaned_data.get("last_name")
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")
        
        user = User.objects.create_user(username,email,password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        print(user)

        profile = profile_form.save(commit=False)
        phone_number = profile_form.cleaned_data.get('phone_number')
        gender = profile_form.cleaned_data.get('gender')
        
        user_profile = UserProfile.objects.get(user = user)
        user_profile.phone_number = phone_number
        user_profile.gender = gender
        user_profile.save()
        
        login(request,user)
        messages.info(request,"Registration Successful...")

        return redirect("index")
    context = {
            "form" : form,
            "profile_form" : profile_form,
        }
    return render(request,"register.html",context)




def loginUser(request):  
    """ LOGIN """

    form = LoginForm(request.POST or None)

    context = {
        "form":form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username,password = password)

        if user is None:
            messages.info(request,"Email or Password is Incorrect")
            return render(request,"login.html",context)

        messages.success(request,"Login Successful")
        login(request,user)
        return redirect("uav:uavs")
    return render(request,"login.html",context)

def logoutUser(request):
    """ LOGOUT """
    logout(request)
    messages.success(request,"Logout Successful")
    return redirect("index")


