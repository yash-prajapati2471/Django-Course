from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,first_name,last_name,username,email,phone_number,password=None):
        if not email:
            raise ValueError("Email is required")
        
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=self.normalize_email(email),
            phone_number=phone_number
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,first_name,last_name,username,email,phone_number,password):
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            phone_number=phone_number,
            email=self.normalize_email(email),
            password=password
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)

class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200,unique=True)

    phone_number = models.CharField(max_length=200)
    address = models.TextField()

    date_joined = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False) 

    def __str__(self):
        return self.email
    
    def has_module_perms(self,add_lable):
        return True
    
    def has_perm(self,perm,obj=None):
        return True
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','username','phone_number']
