from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    nickname = models.CharField()
    email = models.EmailField()
    avatar = models.ImageField(upload_to="avatar/")
    likes_total = models.IntegerField()
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    is_superuser = models.BooleanField()
    date_joined = models.DateField(auto_now_add=True)
    last_login = models.DateField()
