from django.shortcuts import render,redirect
from .models import user
from .forms import RegisterForm,LoginForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializers import userserializers
# Create your views here.

def index(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        query = user(name=name,email=email,password=password)
        query.save()
        
    return render(request,'index.html')

def yash(request):
    if request.method == "POST":
        a = RegisterForm(request.POST)
        if a.is_valid():
            a.save()
            return redirect('login')
    else:
        a = RegisterForm()
    return render(request,'yash.html',{'yash':a})

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

class userview(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = userserializers