# forms.py
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'image', 'description', 'farmer_contact','farmer_name','date_of_posting','location']
        widgets = {
            'date_of_posting': forms.DateInput(attrs={'type': 'date'})
        }

