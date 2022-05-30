import datetime
from django.shortcuts import redirect, render
from .models import Sales
from menu.models import Menu
from .forms import *
from log.models import *
from django.contrib import messages

# Create your views here.

date = datetime.datetime.now()

def sales(request):
    form = SalesForm(request.POST)

    context = {'form' : form}
    if request.method == 'POST':
        if form.is_valid():
            pass
            data = form.save(commit=False)
            data.user = User.objects.get(username=request.user)
            data.save()
            Log.objects.create(user=request.user, activity="Add transaction" , date=date)
            messages.success(request, 'Add transaction')
            return redirect('salesreport')
        else:
            print(form.errors)

    return render(request, 'pos.html', context)

def salesreport(request):
    salesreport = Sales.objects.filter(user = request.user)
    context = {'salesreport' : salesreport}
    return render(request, 'sales.html', context)