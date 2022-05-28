from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('addmenu/', views.addmenu, name='addmenu'),
    path('detailmenu/<int:id>', views.detailmenu, name='detailmenu'),
    path('delete menu/<str:pk>', views.deletemenu, name='deletemenu'),
    path('update menu/<str:pk>', views.updatemenu, name='updatemenu'),
]