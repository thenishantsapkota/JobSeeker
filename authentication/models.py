from django.contrib.auth.models import AbstractUser, User
from django.db import models

# Create your models here.

User._meta.get_field("email")._unique = True


class CustomUser(AbstractUser):
    is_company = models.BooleanField(default=False)
    is_user = models.BooleanField(default=True)
