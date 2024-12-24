from django import forms
from .models import Account


class AccountForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Confirm-Password'}))
    class Meta:
        model = Account
        fields = ['first_name','last_name','username','email','password','phone_number','address']