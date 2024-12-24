from django.http import JsonResponse
from django.shortcuts import render

def home(request):
    friends = ['yash','jay','bhavin']
    return JsonResponse(friends,safe=False)

def index(request):
    return render(request,'ajax.html')