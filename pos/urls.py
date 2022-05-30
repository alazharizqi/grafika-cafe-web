from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.sales, name='sales'),
    path('sales report/', views.salesreport, name='salesreport'),
]