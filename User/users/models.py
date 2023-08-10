from django.db import models
from django.contrib.auth.models import  AbstractBaseUser, UserManager

# Create your models here.
class Users(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=50)

    USERNAME_FIELD = 'username'
    

    objects = UserManager()