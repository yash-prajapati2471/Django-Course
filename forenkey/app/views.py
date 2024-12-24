from django.shortcuts import render,redirect
from .forms import userprofileform,useraddress
from .models import address,user
# Create your views here.

def index(request):
    if request.method == "POST":
        forms = userprofileform(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('second')
    else:
        forms = userprofileform()
    return render(request,'index.html',{'forms':forms})

def second(request):
    if request.method == "POST":
        userid = request.POST['userid']
        addr = request.POST['address']

        try:
            uh = address.objects.get(a=userid)
            uh.address = addr
            uh.save()
            return redirect('/')
        except:
            query = address(a=user(id=userid),address=addr)
            query.save()
            return redirect('/')
    else:
        forms = user.objects.all()
    return render(request,'second.html',{'yash':forms})