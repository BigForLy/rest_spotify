# Generated by Django 4.0.3 on 2022-04-06 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0004_auto_20220406_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artists',
            name='name',
            field=models.TextField(max_length=255),
        ),
    ]
