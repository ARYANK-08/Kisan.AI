from django.contrib import admin
from django.urls import path, include
from .views import chat_with_ai,order
urlpatterns = [
    path('chat_with_ai', chat_with_ai, name='chat_with_ai'),
    path('order', order, name='order'),

]