from django.db import models

# Create your models here.

class employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    work = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class address(models.Model):
    a = models.ForeignKey(employee,on_delete=models.CASCADE)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.address