from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('menu', 'harga', 'status')