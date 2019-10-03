from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from ads_manager.models import VmapConfig, VastFallbackConfig, VmapElement
from trailerhub.main import ABSOLUTE_URL


def vmap(request, id):

    elsconfig = VmapConfig.objects.get(pk=id)
    els = []
    for el_model in elsconfig.vmapelement_set.all():
        el_model: VmapElement
        els.append({
            'type': el_model.type,
            'time_offset': el_model.time_offset,
            'abs_url': ABSOLUTE_URL + reverse('vast_playlist', kwargs={'id': el_model.waterfall_config.id})
        })


    return render(request, template_name='vmap.tpl.xml', context={'els': els})


def vast_playlist(request, id):

    playlist = VastFallbackConfig.objects.get(pk=id)

    urls = playlist.ad_tags.split(sep="\n")


    return render(request, template_name='vast_waterfall.tpl.xml', context={'urls':urls})
