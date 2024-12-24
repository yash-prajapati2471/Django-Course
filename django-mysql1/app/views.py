from django.shortcuts import render
from .models import user
# Create your views here.

def index(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        query = user(name=name,email=email,password=password)
        query.save()

    return render(request,'index.html')

def dashboard(request):
    yash = user.objects.all()
    return render(request,'dashboard.html',{'yash':yash})