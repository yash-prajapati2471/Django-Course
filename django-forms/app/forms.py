from django import forms
from .models import user
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class Form(forms.ModelForm):
    class Meta:
        model = user
        fields = ['name','email','password']

class RegisterForm(UserCreationForm):
    email = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['username','email']

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)

