from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.

class MyAccountManager(BaseUserManager):

    def create_user(self,first_name,last_name,username,email,phone,password=None):

        if not email:
            raise ValueError("User must have an email register")
        
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=self.normalize_email(email),
            phone=phone
        )

        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_superuser(self,first_name,last_name,username,email,phone,password=None):
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            phone=phone,
            email=self.normalize_email(email),
            password=password
        )
        user.is_admin=True
        user.is_staff=True
        user.is_active=True
        user.is_superadmin=True

        user.save(using=self.db)
        return user

class user(AbstractBaseUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200,unique=True)

    phone = models.IntegerField()
    address = models.CharField(max_length=200)

    date_joined = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','username','phone','address']

    def __str__(self):
        return self.email
    
    def has_module_perma(self,add_label):
        return True
    
    def has_perm(self,perm,obj=None):
        return self.is_admin