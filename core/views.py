
from django.shortcuts import render
from django.views import View




def index(request):
    """Home Page"""
    return render(request,"index.html")
