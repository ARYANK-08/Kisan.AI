from django.contrib import admin
from django.urls import path, include
from .views import season,crops,fertilizer,seed,profit,utilized,table
urlpatterns = [
    path('season', season, name='season'),
    path('crops', crops, name='crops'),
    path('fertilizer', fertilizer, name='fertilizer'),
    path('seed', seed, name='seed'),
    path('profit', profit, name='profit'),
    path('utilized', utilized, name='utilized'),
    path('table', table, name='table'),
]