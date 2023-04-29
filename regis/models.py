from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class ManagerUser(BaseUserManager):
    def create_user(self, phone, password, is_active=True, is_superuser=False, is_staff=False, *args, **kwargs):
        user = self.model(
                          password=str(password),
                          phone=phone,
                          is_active=is_active,
                          is_staff=is_staff,
                          is_superuser=is_superuser,
                          **kwargs)
        user.set_password(str(password))
        user.save()
        return user

    def create_superuser(self, phone, password, **kwargs):
        return self.create_user(phone, password, is_superuser=True, is_staff=True, **kwargs)



class User(AbstractUser):
    last_name = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128)
    phone = models.CharField(max_length=12, null=True, blank=True, unique=True)
    password = models.CharField(max_length=128)
    status = models.BooleanField
    username = False
    email = None
    data_joined = models.DateTimeField(editable=False, auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "phone"
    objects = ManagerUser()
    REQUIRED_FIELDS = ['first_name']



    def format(self):
        return {
            "id": self.id,
            "phone": self.phone,
            "first_name": self.first_name,
            "last_name": self.first_name,
            "is_staff": self.is_staff,
            "data_joined": self.data_joined,
            "is_active": self.is_active,
            "is_superuser": self.is_superuser,
        }

    def __str__(self):
        return self.first_name


class Product(models.Model):
    name = models.CharField(max_length=128)
    view = models.IntegerField(default=0)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    price = models.IntegerField()


    def __str__(self):
        return self.name






