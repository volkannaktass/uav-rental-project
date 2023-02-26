from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404, JsonResponse
from django.shortcuts import (HttpResponse, HttpResponseRedirect,
                              get_object_or_404, redirect, render, reverse)
from user.models import UserProfile
from .models import Uav
from django.views.decorators.http import require_http_methods
from .forms import UavForm
from .filters import UavFilter

@login_required(login_url = "user:login")
@require_http_methods(["GET","POST"])
def registerUav(request):
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


    keyword = request.GET.get("keyword")

    if keyword:
        uav_posts = Uav.objects.filter(title__contains = keyword)
        
        return render(request,"show-uav.html",{"uav_posts":uav_posts})
    uav_posts = Uav.objects.all()
    uav_filters = UavFilter(request.GET, queryset=uav_posts)
    return render(request,"show-uav.html",{"uav_filters":uav_filters})


@login_required(login_url = "user:login")
def dashboard(request):
    uav_posts = Uav.objects.filter(author = request.user)
    context = {
        "uav_posts":uav_posts
    }
    return render(request,"dashboard.html",context)


@login_required(login_url = "user:login")
def updateUav(request,id):
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
    uav =get_object_or_404(Uav,id = id,author = request.user)

    uav.delete()

    messages.success(request,"Deleted with Success")

    return redirect("uav:dashboard")
#IMPORTANT
