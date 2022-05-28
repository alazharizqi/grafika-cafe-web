from tkinter import Menu
from django.db import models
from django.utils import timezone
from adminpage.models import User
from menu.models import Menu

# Create your models here.

class Sales(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    trans_code = models.CharField(max_length=200)
    no_meja = models.IntegerField(default=0)
    sub_total = models.FloatField(default=0)
    grand_total = models.FloatField(default=0)
    others = models.FloatField(default=0)
    pay = models.FloatField(default=0)
    change = models.FloatField(default=0)
    date_add = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.trans_code

class SalesItem(models.Model):
    sales_id = models.ForeignKey(Sales, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Menu, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    qty = models.FloatField(default=0)
    total = models.FloatField(default=0)