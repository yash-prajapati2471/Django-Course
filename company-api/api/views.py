from django.shortcuts import render
from rest_framework import viewsets
from .models import company,employee
from .serializers import companyserializers,employeeserializers
# Create your views here.

class companyviewset(viewsets.ModelViewSet):
    queryset = company.objects.all()
    serializer_class = companyserializers

class employeeviewset(viewsets.ModelViewSet):
    queryset = employee.objects.all()
    serializer_class = employeeserializers