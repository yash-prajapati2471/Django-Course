from django.shortcuts import render,redirect
from .models import *
from .forms import userForm
# Create your views here.

def index(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        query = user(name=name,email=email,password=password)
        query.save()
        return redirect('second')
    return render(request,'index.html')

def second(request):
    if request.method == "POST":
        id = request.POST['id']
        img = request.FILES['img']
        address = request.POST['address']

        query1 = userprofile(a_id=id,img=img,address=address)
        query1.save()
        return redirect('index')
    else:
        forms = user.objects.all()
    return render(request,'second.html',{'yash':forms})

def dashboard(request):
    abc = userprofile.objects.all()
    return render(request,'dashboard.html',{'jay':abc})

def edit(request,id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        img = request.FILES['images']
 
        uh = userprofile.objects.get(id=id)
        uh.img = img
        uh.address = address
        uh.save()

        uy = user.objects.get(id=uh.id)
        uy.name = name
        uy.email = email
        uy.password = password
        uy.save()
        return redirect('dashboard')
    
    xyz = userprofile.objects.get(id=id)
    return render(request,'edit.html',{'raj':xyz})

def Form(request):
    if request.method == "POST":
        data = userForm(request.POST)
        if data.is_valid():
            data.save()
            return redirect('dashboard')
    else:
        data = userForm()
    return render(request,'form.html',{'hello':data})