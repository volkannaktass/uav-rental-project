
from django.contrib.auth.decorators import login_required
from django.shortcuts import (HttpResponse, HttpResponseRedirect,
                              get_object_or_404, redirect, render, reverse)
from django.views import View




def index(request):
    return render(request,"index.html")
