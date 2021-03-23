from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.db import IntegrityError
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.
class CustomUserManager(BaseUserManager):
    def get_or_create_for_cognito(self, cognito_id: str, email: str):
        try:
            return self.get(cognito_id=cognito_id)
        except self.model.DoesNotExist:
            pass

        try:
            user = self.create(
                cognito_id=cognito_id,
                email=email)
        except IntegrityError:
            user = self.get(cognito_id=cognito_id)

        return user


class CustomUser(AbstractBaseUser):
    cognito_id = models.CharField(max_length=128, blank=True)
    email = models.EmailField(('email address'), unique=True)

    objects = CustomUserManager()
