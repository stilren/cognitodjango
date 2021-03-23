from django.db import models
from django.contrib.auth.models import AbstractUser

class Chore(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)