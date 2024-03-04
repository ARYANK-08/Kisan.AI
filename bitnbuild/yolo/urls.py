
# Create your views here.
from django.contrib import admin
from django.urls import path, include
from .views import out_of_stock

urlpatterns = [
    path('out_of_stock', out_of_stock, name='out_of_stock'),

]