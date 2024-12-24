from django.contrib import admin
from .models import *
# Register your models here.

class yash(admin.ModelAdmin):
    list_display = ['name','email','password']
admin.site.register(user,yash)

admin.site.register(userprofile)