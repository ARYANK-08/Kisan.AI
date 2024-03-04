from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'image', 'price', 'quantity_total', 'date_bought', 'date_expiration', 'category', 'quantity_remaining']
