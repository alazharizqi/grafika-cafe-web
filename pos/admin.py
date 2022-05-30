from django.contrib import admin
from .models import *

# Register your models here.

# @admin.register(Sales)
# class MenuAdmin(admin.ModelAdmin):
#     list_display = ('trans_code')

# @admin.register(SalesItem)
# class MenuAdmin(admin.ModelAdmin):
#     list_display = ('sales_id')

admin.site.register(Sales)