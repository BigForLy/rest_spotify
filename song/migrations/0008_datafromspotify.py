# Generated by Django 4.0.3 on 2022-04-06 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0007_alter_releases_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataFromSpotify',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_loading', models.DateTimeField(verbose_name='time_loading')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
