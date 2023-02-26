from django import forms
from django.contrib.auth.models import User 
from .models import UserProfile
from django.db import models



class LoginForm(forms.Form):
     username = forms.CharField(label = "Username")
     password = forms.CharField(label = "Password",widget = forms.PasswordInput)




class RegisterForm(forms.Form):
    
    username = forms.CharField(max_length = 50,label = "Username:")
    password = forms.CharField(max_length=20,label = "Password:",widget = forms.PasswordInput)
    confirm = forms.CharField(max_length=20,label = "Confirm Password:",widget = forms.PasswordInput)
    email = forms.EmailField(widget=forms.TextInput(),label=("Email address:"))
    first_name = forms.CharField(max_length = 100,label = "Name:")
    last_name = forms.CharField(max_length=100,label="Surname:")

    def clean(self):
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")
        email = self.cleaned_data.get("email")
        
        user = User.objects.filter(username=username)
        if user.exists():
            raise forms.ValidationError("That user is already taken")
        long = len(User.objects.filter(email=email))
        if password and confirm and password != confirm:
            raise forms.ValidationError("Passwords Do Not Match")
        elif long > 0:
            raise forms.ValidationError('This E-mail Has Already Been Used')
        
        values = {
            'first_name' : first_name,
            "last_name" : last_name,
            "username" : username,
            "password" : password,
            "email" : email,           
        }
        return values


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone_number','gender')




