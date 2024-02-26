from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    username = models.CharField(max_length=200, default='user')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class RoomType(models.Model):
    name = models.CharField(max_length=200)

class Room(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    type = models.ForeignKey(RoomType,on_delete=models.SET_NULL,null=True)
    floor = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    