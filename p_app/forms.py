from dataclasses import fields

from django import forms
from . models import Orders, Seller


class  checkoutform(forms.ModelForm):
    class Meta:
        model=Orders
        fields=["address","mobile"]

from .models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class OrderForm(forms.Form):
    quantity = forms.IntegerField(label='Quantity', min_value=1)
