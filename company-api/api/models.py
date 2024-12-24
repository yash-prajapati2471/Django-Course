from django.db import models

# Create your models here.

class company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    phone = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return self.name