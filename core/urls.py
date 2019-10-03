from django.contrib import admin
from django.urls import path, include

from core.views import index, detail, vmap, vast_playlist

urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:id>', detail, name='trailer_detail'),
    path('vmap', vmap, name='vmap_old'),
    path('vast_playlist.xml', vast_playlist, name='vast_playlist_old'),
]
