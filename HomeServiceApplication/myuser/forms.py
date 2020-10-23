from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

class UserRegistrationFrm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','password1','password2']


class LoginFrm(forms.Form):
    email=forms.CharField(max_length=120)
    password=forms.CharField(widget=forms.PasswordInput)
