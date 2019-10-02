from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from core.models import Trailer


def index(request):
    return render(request, template_name='index.html', context={})


def detail(request, id):
    trailer = Trailer.objects.get(id=id)
    video_url = trailer.video.url
    return render(request, template_name='detail.html', context={
        'id': id,
        'video_url': video_url
    })


def vmap(request):
    return render(request, template_name='vmap.xml', context={})


def vast_playlist(request):
    return render(request, template_name='vast_waterfall.xml', context={})
