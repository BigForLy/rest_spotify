# Generated by Django 4.0.3 on 2022-04-12 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0009_rename_artists_artistsinstance_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagesInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url64', models.URLField(verbose_name='url 64x64')),
                ('url300', models.URLField(verbose_name='url 300x300')),
                ('url640', models.URLField(verbose_name='url 640x640')),
            ],
        ),
        migrations.DeleteModel(
            name='Images',
        ),
        migrations.RemoveField(
            model_name='releasesinstance',
            name='images',
        ),
        migrations.AddField(
            model_name='releasesinstance',
            name='images',
            field=models.ManyToManyField(to='song.imagesinstance'),
        ),
    ]