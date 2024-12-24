from django import forms
from .models import user,address

class userprofileform(forms.ModelForm):
    class Meta:
        model = user
        fields = "__all__"

class useraddress(forms.ModelForm):
    class Meta:
        model = address
        fields = "__all__"