from django.db import models

# Create your models here.


class VmapConfig(models.Model):
    label = models.fields.TextField()

    def __str__(self):
        return self.label


class VastFallbackConfig(models.Model):
    label = models.fields.TextField()
    ad_tags = models.fields.TextField()

    def __str__(self):
        return self.label


class VmapElement(models.Model):
    type = models.fields.CharField(choices=(
        ('preroll', 'preroll'),
        ('midroll', 'midroll'),
        ('postroll', 'postroll'),
    ), max_length=128)

    time_offset = models.fields.CharField(choices=(
        ('start', 'start'),
        ('00:00:15.000', '15 sec'),
        ('00:00:30.000', '30 sec'),
        ('end', 'end'),
    ), default='start', max_length=128)

    ad_tag = models.fields.TextField(null=True, blank=True)
    waterfall_config = models.ForeignKey(to=VastFallbackConfig, on_delete=models.CASCADE, null=True)
    parent = models.ForeignKey(to=VmapConfig, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.parent.label} {self.get_type_display()} {self.waterfall_config.label}"
