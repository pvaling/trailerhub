from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.cache import cache_page

from core.models import Trailer


@cache_page(timeout=10)
def index(request):




    context = {
        'random_list': Trailer.objects.all().order_by("?")[:30],
        'carousel': Trailer.objects.filter()[0:7],
        'main_vid': Trailer.objects.first(),
        'featured': Trailer.objects.all().order_by("?")[:4],
    }

    return render(request, template_name='index.html', context=context)

@cache_page(timeout=10)
def detail(request, id):
    trailer = Trailer.objects.get(id=id)
    video_url = trailer.video.url

    context = {
        'random_list': Trailer.objects.all().order_by("?")[:30],
        'carousel': Trailer.objects.filter()[0:7],
        'main_vid': Trailer.objects.first(),
        'featured': Trailer.objects.all().order_by("?")[:4],
        'id': id,
        'trailer': trailer,
        'video_url': video_url
    }

    return render(request, template_name='detail.html', context=context)


def vmap(request):
    return render(request, template_name='vmap.xml', context={})


def vast_playlist(request):
    return render(request, template_name='vast_waterfall.xml', context={})
