from rest_framework import serializers
from .models import company,employee

class companyserializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = company
        fields = ['name','email','password']

class employeeserializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = employee
        fields = "__all__"