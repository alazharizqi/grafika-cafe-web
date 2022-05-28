from django import forms
from django.db.models import fields
from django.forms import ModelForm
from django import forms
from . models import *

class MenuForm(ModelForm):
    class Meta:
        model = Menu
        fields = [
            'id', 'user', 'menu', 'harga', 'deskripsi', 'status', 'kategori', 'kode',
        ]

        widgets = {
            'menu' : forms.TextInput( attrs={'class':'form-control', 'placeholder':'Menu'}),
            'harga' : forms.TextInput( attrs={'class':'form-control', 'placeholder':'Price'}),
            'kode' : forms.TextInput( attrs={'class':'form-control', 'placeholder':'Code'}),
            'deskripsi' : forms.Textarea( attrs={'class':'form-control', 'placeholder':'Description'}),
            'status' : forms.Select( attrs={'class':'form-control'}),
            'kategori' : forms.Select( attrs={'class':'form-control'}),
        }