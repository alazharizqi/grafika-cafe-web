from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    roles = (
        ('Admin', 'Admin'),
        ('Manager', 'Manager'),
        ('Kasir', 'Kasir'),
    )

    role = models.CharField(max_length=200, choices=roles, null=True, blank=True)

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        super().save()