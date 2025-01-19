from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
from django.db import models


class User(AbstractUser):
    avatar = models.ImageField(upload_to="avatar/", blank=True)
    likes_total = models.IntegerField(default=0)
    first_name = None
    last_name = None
    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"


class CustomUserManager(UserManager):
    pass
