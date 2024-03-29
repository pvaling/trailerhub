# Generated by Django 2.2.5 on 2019-10-01 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190928_2305'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsitem',
            name='picture',
            field=models.ImageField(null=True, upload_to='files/news_images'),
        ),
        migrations.AlterField(
            model_name='trailer',
            name='video',
            field=models.FileField(upload_to='files/trailers'),
        ),
    ]
