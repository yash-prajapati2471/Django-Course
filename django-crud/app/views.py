from django.shortcuts import render,redirect
from .forms import register,RegisterForm,LoginForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from .models import user

# Create your views here.

def index(request):
    if request.method == "POST":
        data = register(request.POST)
        if data.is_valid():
            data.save()
            return redirect('read')
    else:
        data = register()
    return render(request,'index.html',{'yash':data})

def read(request):

    datau = user.objects.all()

    return render(request,'read.html',{'data':datau})

def edit(request,id):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        uh = user.objects.get(id=id)
        uh.name = name
        uh.email = email
        uh.password = password
        uh.save()
        return redirect('read')
    
    xyz = user.objects.get(id=id)

    return render(request,'edit.html',{'jay':xyz})

def delete(request,id):

    ab = user.objects.get(id=id)
    ab.delete()
    return redirect('read')

def signup(request):
    if request.method == "POST":
        dataa = RegisterForm(request.POST)
        if dataa.is_valid:
            dataa.save()
            return redirect('read')
    else:
        dataa = RegisterForm()
    return render(request,'signup.html',{'form':dataa})

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
    return render(request,'login.html',{'forms':forms})

def dashboard(request):
    return render(request,'dashboard.html')