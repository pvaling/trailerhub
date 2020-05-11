from django.urls import path, include

from ads_manager.views import vmap, vast_playlist

urlpatterns = [
    path('vmap/<int:id>/xml', vmap, name='vmap'),
    path('vast_playlist/<int:id>/xml', vast_playlist, name='vast_playlist'),
]
