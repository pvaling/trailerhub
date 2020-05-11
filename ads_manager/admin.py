from django.contrib import admin

# Register your models here.
from ads_manager.models import VmapConfig, VastFallbackConfig, VmapElement

admin.site.register(VmapConfig)
admin.site.register(VmapElement)
admin.site.register(VastFallbackConfig)
