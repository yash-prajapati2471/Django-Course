from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['username','email']

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200)