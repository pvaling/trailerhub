import datetime

from django.contrib.auth import get_user_model
from django.core.files import File
from django.db import models

# Create your models here.
from django.db.models import TextField, IntegerField, FileField, ForeignKey, PROTECT, DateTimeField, ImageField, \
    CharField


class UGCMixin(models.Model):
    author = ForeignKey(to=get_user_model(), default=1, on_delete=PROTECT)
    created_at = DateTimeField(auto_now_add=True, null=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Trailer(UGCMixin):
    label = TextField()
    description = TextField()
    year = IntegerField()
    video = FileField(upload_to='files/trailers', null=True)
    cover = ImageField(upload_to='files/covers', null=True)
    source_id = CharField(max_length=256, default='', null=True)
    imdb_id = CharField(max_length=256, default='', null=True)

    @property
    def ui_badge(self):
        return None

    def __str__(self):
        return self.label


class NewsItem(UGCMixin):
    label = TextField()
    content = TextField()
    source_link = TextField()
    picture = ImageField(upload_to='files/news_images', null=True)
