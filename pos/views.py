from django.shortcuts import render
from menu.models import *
from pos.models import Sales

# Create your views here.

def pos(request):
    menu = Menu.objects.filter(status= 'Available')
    context = {'menu' : menu}
    return render(request, 'pos.html', context)

def sales(request):
    sales = Sales.objects.filter(user = request.user)
    context = {'sales' : sales}
    return render(request, 'sales.html', context)