from django.db import models

# Create your models here.

class user(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class userprofile(models.Model):
    a = models.ForeignKey(user,on_delete=models.CASCADE)
    img = models.ImageField(upload_to='img/',blank=True,null=True)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.address
    
