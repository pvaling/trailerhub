# Generated by Django 2.2.5 on 2019-10-02 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_trailer_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trailer',
            name='video',
            field=models.FileField(null=True, upload_to='files/trailers'),
        ),
    ]