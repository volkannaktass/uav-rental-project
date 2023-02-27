from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.shortcuts import (get_object_or_404, redirect, render, reverse)
from user.models import UserProfile
from .models import Uav
from django.views.decorators.http import require_http_methods
from .forms import UavForm
from .filters import UavFilter

@login_required(login_url = "user:login")
@require_http_methods(["GET","POST"])
def registerUav(request):
    """Registration UAV rent"""
    """Get the new obj from the
       form and control the form
       then save the form.
       Then render to related page
    """
    uavForm = UavForm(request.POST or None,request.FILES or None)
    if uavForm.is_valid():
        uav = uavForm.save(commit=False)
        uav.author = request.user
        uav.save()
       
        messages.success(request,"The UAV was registered successfully!")
        return redirect("uav:dashboard")
    context = {    
        "uavForm":uavForm,
    } 
    return render(request,"register-uav.html",context)
    



@login_required(login_url = "user:login")
def showUav(request):
    """ Listing """
    """Get the specific keyword from the template
    then make a query with filter(). If the title contains the
    keyword, return the related uav.
    In the else statement, get the all objects then filter with
    UavFilter which is in the filters.py and send to show page.If it hasnt
    got any filter, send all uav to the show page
    """

    keyword = request.GET.get("keyword")

    if keyword:
        uav_search = Uav.objects.filter(title__contains = keyword)
        
        return render(request,"show-uav.html",{"uav_search":uav_search})
    else:
        uav_posts = Uav.objects.all()
        uav_filters = UavFilter(request.GET, queryset=uav_posts)
        return render(request,"show-uav.html",{"uav_filters":uav_filters})




@login_required(login_url = "user:login")
def dashboard(request):
    
    """ Control Panel-UAV Registration"""
    """ Receives uav posts of the logged in
    user and sends them to the table on the
    uav registration page
    """
    uav_posts = Uav.objects.filter(author = request.user)
    context = {
        "uav_posts":uav_posts
    }
    return render(request,"dashboard.html",context)


@login_required(login_url = "user:login")
def updateUav(request,id):
    """ Updating"""
    """This function gets the
    obj with id and changes the
    value with new one then saves it
    """
    uav = get_object_or_404(Uav,id = id,author = request.user)
    form = UavForm(request.POST or None,request.FILES or None,instance=uav)

    if form.is_valid():
        uav_posts = form.save(commit=False)
        uav_posts.author = request.user
        uav_posts.save()

        messages.success(request,"Updated with Success")
        return redirect("uav:dashboard")
    context = {
        "form":form,
               } 

    return render(request,"update.html",context)




@login_required(login_url = "user:login")
def deleteUav(request,id):
    """ Deleting"""
    """ Get the object with
    id and user then delete it from db.
    """
    uav =get_object_or_404(Uav,id = id,author = request.user)

    uav.delete()

    messages.success(request,"Deleted with Success")

    return redirect("uav:dashboard")

