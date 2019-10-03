import os
import uuid

from django.core.files import File
from django.core.management.base import BaseCommand, CommandError
from core.models import Trailer
import requests
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


class Command(BaseCommand):
    help = 'Grab '

    def add_arguments(self, parser):
        parser.add_argument('count', nargs='+', type=int)

    def handle(self, *args, **options):

        url = "https://www.kinomania.ru/trailers"

        querystring = {"handler": "search"}

        payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"filter\"\r\n\r\n{\"page\":1}\r\n-----011000010111000001101001--\r\n"
        headers = {
            'accept': "application/json",
            'content-type': "multipart/form-data; boundary=---011000010111000001101001",
            'x-requested-with': "XMLHttpRequest"
        }

        response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

        for item in response.json():
            import urllib.request
            video = urllib.request.urlretrieve('http:' + item[5])
            image = urllib.request.urlretrieve('http:' + item[4])

            new_trailer = Trailer(
                label=item[9],
                source_id=item[0],
                year=2019
            )
            new_trailer.cover.save(
                str(uuid.uuid4()) + '.' + item[4].split('.')[-1],
                File(open(image[0], 'rb'))
            )
            new_trailer.video.save(
                str(uuid.uuid4()) + '.' + item[5].split('.')[-1],
                File(open(video[0], 'rb'))
            )

            new_trailer.save()
            print(new_trailer)
