from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    name = models.CharField(null=True, blank=True, max_length=100)
