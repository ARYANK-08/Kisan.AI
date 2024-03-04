from django.contrib import admin
from django.urls import path, include

from .views import index, add_inventory, display_inventory,generate_pdf, gemini, ulogin, dashboard, make_pickaxe, make_pickaxe_page,weather_forecast

urlpatterns = [
    path('', index, name='index'),
    path('add_inventory', add_inventory, name='add_inventory'),
    path('display_inventory', display_inventory, name='display_inventory'),

    path('ulogin', ulogin, name='ulogin'),
    path('dashboard', dashboard, name='dashboard'),

    path('generate_pdf', generate_pdf, name='generate_pdf'),
    path('gemini', gemini, name='gemini'),

    path('make_pickaxe_page/', make_pickaxe_page, name='make_pickaxe_page'),
    path('make_pickaxe/', make_pickaxe, name='make_pickaxe'),

    path('weather', weather_forecast, name='weather_forecasting'),

]