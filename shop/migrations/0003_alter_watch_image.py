# Generated by Django 3.2.18 on 2023-04-12 23:44

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_watch_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watch',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, default='placeholder', max_length=255),
        ),
    ]
