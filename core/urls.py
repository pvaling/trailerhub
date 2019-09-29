from django.contrib import admin
from django.urls import path, include

from core.views import index, detail

urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:id>', detail, name='detail'),
]
