from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'image', 'description', 'farmer_contact','farmer_name','date_of_posting','location']  # Customize the fields displayed in the admin list

admin.site.register(Product, ProductAdmin)

# Register your models here.
