from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *

# Create your views here.

def menu(request):
    menu = Menu.objects.all()
    context = {'menu' : menu}
    return render(request, 'menu.html', context)

@login_required(login_url='login')
def addmenu(request):
    form = MenuForm(request.POST)

    context = {'form' : form}
    if request.method == 'POST':
        if form.is_valid():
            pass
            data = form.save(commit=False)
            data.user = User.objects.get(username=request.user)
            data.save()
            return redirect('menu')
        else:
            print(form.errors)

    return render(request, 'addmenu.html', context)

@login_required(login_url='login')
def detailmenu(request, id):
    menu = Menu.objects.get(id=id)
    context = {'menu' : menu}
    return render(request, 'detailmenu.html', context)

@login_required(login_url='login')
def deletemenu(request, pk):
    menu = Menu.objects.get(id=pk)
    if request.method =='POST':
        menu.delete()
        return redirect('menu')
    context = {'menu':menu}
    return render(request, 'deletemenu.html', context)

@login_required(login_url='login')
def updatemenu(request, pk):

    menu = Menu.objects.get(id=pk)
    form = MenuForm(instance=menu)

    if request.method == 'POST':
        form = MenuForm(request.POST, instance=menu)
        if form.is_valid():
            form.save()
            return redirect('menu')

    context = {'form': form}
    return render(request, 'updatemenu.html', context)