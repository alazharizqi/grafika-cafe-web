from datetime import date
from django.shortcuts import redirect, render
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib import messages
from log.models import *
from adminpage.models import User
from .forms import *
import datetime

# Create your views here.

date = datetime.datetime.now()

def login(request):
    form = LoginForm(request.POST)

    if request.method == "POST":
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = User.objects.get(username = username)

            if user is not None and user.role == "Admin" and username == username and password == password:
                auth_login(request, user)
                Log.objects.create(user=request.user, activity="Login" , date=date)
                messages.success(request, 'Login')
                return redirect('admin')
            elif user is not None and user.role == "Manager" and username == username and password == password:
                auth_login(request, user)
                Log.objects.create(user=request.user, activity="Login" , date=date)
                messages.success(request, 'Login')
                return redirect('menu')
            elif user is not None and user.role == "Kasir" and username == username and password == password:
                auth_login(request, user)
                Log.objects.create(user=request.user, activity="Login" , date=date)
                messages.success(request, 'Login')
                return redirect('sales')
            else:
                messages.info(request, 'Wrong username or password')

    context = {'form':form}
    return render(request, 'login.html', context)

def logoutuser(request):
    Log.objects.create(user=request.user, activity="Logout" , date=date)
    messages.success(request, 'Logout')
    logout(request)
    return redirect('login')