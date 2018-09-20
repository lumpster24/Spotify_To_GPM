# Generated by Django 2.0 on 2018-09-19 23:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('spotify_to_gpm_app', '0003_auto_20180910_1026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gpmuser',
            name='spotify_user',
        ),
        migrations.AddField(
            model_name='gpmuser',
            name='spotify_user',
            field=models.ManyToManyField(related_name='GPMUser', to=settings.AUTH_USER_MODEL),
        ),
    ]