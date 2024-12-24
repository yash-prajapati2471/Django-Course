from rest_framework import routers
from .views import *
from django.urls import path,include

router = routers.DefaultRouter()
router.register(r'employee',employeeviewset)

urlpatterns = [
    path('',include(router.urls)),
    path('index',index,name='index'),
    path('second',second,name='second'),
]