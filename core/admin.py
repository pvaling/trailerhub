from django.contrib import admin

# Register your models here.
from core.models import Trailer, NewsItem

admin.site.register(Trailer)
admin.site.register(NewsItem)
