from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    email_active_code = models.CharField(max_length=100, verbose_name="Email activation code")

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        if self.get_full_name() is not "":
            return self.email
