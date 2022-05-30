from django import forms
from django.forms import ModelForm
from django import forms
from . models import *

class SalesForm(ModelForm):
    class Meta:
        model = Sales

        fields = [
            'customer', 'no_meja', 'menu', 'qty', 'total',
        ]

        widgets = {
            'customer' : forms.TextInput( attrs={'class':'form-control', 'placeholder':'Customer'}),
            'no_meja' : forms.TextInput( attrs={'class':'form-control', 'type' : 'number', 'placeholder':'Table Number', 'min' : '1', 'value' : '1'}),
            'menu' : forms.Select( attrs={'class':'form-control'}),
            # 'kode_menu' : forms.TextInput( attrs={'class':'form-control', 'placeholder':'Code', 'disabled' : 'True',}),
            # 'kategori' : forms.TextInput( attrs={'class':'form-control', 'placeholder':'Category', 'disabled' : 'True',}),
            # 'harga' : forms.TextInput( attrs={'class':'form-control', 'placeholder':'Price', 'disabled' : 'True',}),
            # 'status' : forms.TextInput( attrs={'class':'form-control', 'placeholder':'Status', 'disabled' : 'True',}),
            'qty' : forms.TextInput( attrs={'class':'form-control', 'type' : 'number', 'placeholder':'Qty', 'min' : '1', 'value' : '1'}),
            'total' : forms.TextInput( attrs={'class':'form-control', 'placeholder':'Total'}),
        }