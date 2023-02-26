from django import forms
from .models import Uav
from django.db import models

### Created to show fields about uav in the templates
class UavForm(forms.ModelForm):
    class Meta:
        ### Connect the uav model with form
        model = Uav
        fields = ["title","brand","model","weight","category","price","content","image"]


