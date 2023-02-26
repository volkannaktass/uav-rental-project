from django import forms
from .models import Uav
from django.db import models


class UavForm(forms.ModelForm):
    class Meta:
        model = Uav
        fields = ["title","brand","model","weight","category","price","content","image"]


