from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    if request.method == "POST":
        forms = RegisterForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('login')
    else:
        forms = RegisterForm()
    return render(request,'index.html',{'yash':forms})

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

@login_required(login_url='login')
def dashboard(request):
    return render(request,'dashboard.html')