import datetime
from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from log.models import *

# Create your views here.

date = datetime.datetime.now()

@login_required(login_url='login')
def admin(request):
    user = User.objects.all()
    context = {'user' : user}
    return render(request, 'admin.html', context)

@login_required(login_url='login')
def adduser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')
        hash_password = make_password(password)

        User.objects.create(
            username=username, email=email, password=password, role=role)
        Log.objects.create(user=request.user, activity="Add user" , date=date)
        messages.success(request, 'Add user')

        return redirect('admin')
    
    return render(request, 'adduser.html')

@login_required(login_url='login')
def detailuser(request, id):
    user = User.objects.get(id=id)
    context = {'user' : user}
    return render(request, 'detailuser.html', context)

@login_required(login_url='login')
def deleteuser(request, pk):
    user = User.objects.get(id=pk)
    if request.method =='POST':
        user.delete()
        Log.objects.create(user=request.user, activity="Delete user" , date=date)
        messages.success(request, 'Delete user')
        return redirect('admin')
    context = {'user':user}
    return render(request, 'deleteuser.html', context)

@login_required(login_url='login')
def updateuser(request, id):
    form = User.objects.get(id=id)
    print(form)
    context = {
        'form' : form
    }
    if request.method == 'POST':
        # userid = request.POST.get('id')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')
        hash_password = make_password(password)

        userr = User.objects.get(id=id)
        userr.username = username
        userr.email = email
        userr.password = hash_password
        userr.role = role
        userr.save()
        Log.objects.create(user=request.user, activity="Update user" , date=date)
        messages.success(request, 'Update user')

        return redirect('admin')

    return render(request, 'updateuser.html', context)

def logadmin(request):
    log = Log.objects.all()
    context = {'log' : log}
    return render(request, 'logadmin.html', context)