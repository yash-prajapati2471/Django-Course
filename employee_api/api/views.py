from django.shortcuts import render,redirect
from rest_framework import viewsets
from .models import employee,address
from .serializers import employeeserializers
from .forms import employeeform
# Create your views here.

class employeeviewset(viewsets.ModelViewSet):
    queryset = employee.objects.all()
    serializer_class = employeeserializers

def index(request):
    if request.method == "POST":
        forms = employeeform(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('second')
    else:
        forms = employeeform()
    return render(request,'index.html',{'yash':forms})

def second(request):
    if request.method == "POST":
        userid = request.POST['userid']
        addr = request.POST['address']
        print(userid)

        query = address(a=employee(employee_id=userid),address=addr)
        query.save()
        return redirect('index')
    else:
        userid = employee.objects.all()
    return render(request,'second.html',{'jay':userid})