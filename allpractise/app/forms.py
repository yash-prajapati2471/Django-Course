from django import forms
from .models import userprofile

class userForm(forms.ModelForm):
    class Meta:
        model = userprofile
        fields = "__all__"