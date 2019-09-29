from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, template_name='index.html', context={})


def detail(request, id):
    return render(request, template_name='detail.html', context={id: id})

