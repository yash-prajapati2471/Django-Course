from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from .views import companyviewset,employeeviewset

router = routers.DefaultRouter()
router.register(r'company',companyviewset)

router1 = routers.DefaultRouter()
router1.register(r'employee',employeeviewset)

urlpatterns = [
    path('',include(router.urls)),
    path('employee',include(router1.urls)),
]