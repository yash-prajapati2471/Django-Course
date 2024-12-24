from django.shortcuts import render,redirect
from .forms import Form
from .models import user
from .forms import RegisterForm,LoginForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
# Create your views here.

def index(request):
    if request.method == "POST":
        data = Form(request.POST)
        if data.is_valid():
            data.save()
            return redirect('dashboard')
    else:
        data = Form()
    return render(request,'index.html',{'yash':data})

def dashboard(request):
    a = user.objects.all()
    return render(request,'dashboard.html',{'b':a})

def signup(request):
    if request.method == "POST":
        dataa = RegisterForm(request.POST)
        if dataa.is_valid():
            dataa.save()
            return redirect('dashboard')
    else:
        dataa = RegisterForm()
    return render(request,'signup.html',{'c':dataa})

def login(request):
    forms = LoginForm()
    if request.method == "POST":
        forms = LoginForm(request,data=request.POST)
        if forms.is_valid():
            username = forms.cleaned_data.get('username')
            password = forms.cleaned_data.get('password')

            user = authenticate(request,username=username,password=password)
            if user is not None:
                auth_login(request,user)
                return redirect('dashboard')
            else:
                pass

    return render(request,'login.html',{'jay':forms})

