from django.contrib.auth.models import AbstractUser
from django.db import models

class MyUser(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    img_porfile = models.ImageField(upload_to='user', blank=True)

    def __str__(self):
        return self.username
