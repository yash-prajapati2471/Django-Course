from django import forms
from .models import user

class AccountForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ['first_name','last_name','username','email','phone','password']