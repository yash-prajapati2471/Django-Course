from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate

# Create your views here.

def register(request):
    if request.method == "POST":
        name = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        conpassword = request.POST['conpassword']

        if password == conpassword:
            users = User.objects.create_user(name,email,password)
            users.save()
        else:
            pass
    return render(request,'register.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        a = authenticate(username=username,password=password)

        if a is not None:
            auth_login(request,a)
            return redirect(dashboard)
        else:
            pass
    return render(request,'login.html')

def dashboard(request):
    return render(request,'dashboard.html')