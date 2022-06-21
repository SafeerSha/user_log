from calendar import c
from operator import mod
from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User, AbstractUser, BaseUserManager
from django.utils import timezone
from django.forms import modelformset_factory

class user(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE)
    created = models.DateField(default=timezone.now)
    
    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.user.username

class lastlogin(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE)
    lastlogin = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class lastlogout(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE)
    lastlogout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
