# Generated by Django 3.0.4 on 2020-08-15 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OfflinePlaylist', '0006_remove_song_downloaded'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='downloaded',
            field=models.BooleanField(default=False),
        ),
    ]
