from django.shortcuts import render
from .forms import AccountForm
from django.http import HttpResponse
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("User are created")
    else:
        form = AccountForm()
    return render(request,'index.html',{'form':form})