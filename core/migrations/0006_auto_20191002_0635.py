# Generated by Django 2.2.5 on 2019-10-02 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20191002_0601'),
    ]

    operations = [
        migrations.AddField(
            model_name='trailer',
            name='imdb_id',
            field=models.CharField(default='', max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='trailer',
            name='source_id',
            field=models.CharField(default='', max_length=256, null=True),
        ),
    ]