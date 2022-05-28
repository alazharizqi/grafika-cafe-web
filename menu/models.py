from django.db import models
from adminpage.models import *

# Create your models here.


class Menu(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    kode = models.CharField(max_length=200, null=True, blank=True)
    menu = models.CharField(max_length=200, null=True, blank=True)
    kategoris = (
        ('Food', 'Food'),
        ('Drink', 'Drink'),
        ('Snacks', 'Snacks'),
    )

    kategori = models.CharField(max_length=200, choices=kategoris, null=True, blank=True)
    harga = models.FloatField(null=True, blank=True)
    deskripsi = models.TextField(null=True, blank=True)
    
    statuss = (
        ('Available', 'Available'),
        ('Unavailable', 'Unavailable'),
    )

    status = models.CharField(max_length=200, default='Tersedia', choices=statuss, null=True, blank=True)

    def save(self, *args, **kwargs):
        super(Menu, self).save(*args, **kwargs)
        super().save()