from tkinter import CASCADE, Menu
from django.db import models
from django.utils import timezone
from adminpage.models import User
from menu.models import Menu
from django.utils.crypto import get_random_string

# Create your models here.

class Sales(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    customer = models.CharField(max_length=200, null=True, blank=True)
    no_meja = models.IntegerField(default=0)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True, blank=True)
    qty = models.IntegerField(default=0)
    total = models.FloatField(default=0)
    date_add = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        super(Sales, self).save(*args, **kwargs)
        self.slug = get_random_string(10, '0123456789')
        super().save()