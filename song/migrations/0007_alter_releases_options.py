# Generated by Django 4.0.3 on 2022-04-06 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0006_releases_artists_delete_crartistsandreleases'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='releases',
            options={'ordering': ['-release_date']},
        ),
    ]