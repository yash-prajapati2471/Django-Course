from django import forms
from .models import *

class employeeform(forms.ModelForm):
    class Meta:
        model = employee
        fields = "__all__"