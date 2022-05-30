from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.admin, name='admin'),
    path('add user/', views.adduser, name='adduser'),
    path('activity admin/', views.logadmin, name='logadmin'),
    path('detail user/<int:id>', views.detailuser, name='detailuser'),
    path('delete user/<str:pk>', views.deleteuser, name='deleteuser'),
    path('update user/<int:id>', views.updateuser, name='updateuser'),
]