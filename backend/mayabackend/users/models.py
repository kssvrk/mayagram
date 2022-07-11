from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class MayaUser(AbstractUser):

    email = models.EmailField(verbose_name='email address', unique=True)
    #username = models.CharField(max_length=30, unique=True,default='test')
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    status=models.CharField(max_length=50)
    REQUIRED_FIELDS = ('username',)

    USERNAME_FIELD='email'