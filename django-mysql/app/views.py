from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import user
from .forms import RegisterForm,LoginForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        query = user(name=name,email=email,password=password)
        query.save()
        return HttpResponse("Data has successful stored!")
    
    return render(request,'index.html')

def forms(request):
    if request.method == "POST":
        a = RegisterForm(request.POST)
        if a.is_valid():
            a.save()
            return HttpResponse("Welcome")
    else:
        a = RegisterForm()
    return render(request,'forms.html',{'yash':a})

def login(request):
    b = LoginForm()
    if request.method == "POST":
        b = LoginForm(request,data=request.POST)
        if b.is_valid():
            username = b.cleaned_data.get('username')
            password = b.cleaned_data.get('password')

            user = authenticate(request,username=username,password=password)
            if user is not None:
                auth_login(request,user)
                return redirect('dashboard')
            else:
                pass
    return render(request,'login.html',{'jay':b})

@login_required(login_url='login')
def dashboard(request):
    return render(request,'dashboard.html')