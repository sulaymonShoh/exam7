from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar = models.FileField(upload_to="users/avatar/%Y/%m/%d")
