# Generated by Django 3.2.18 on 2023-04-16 22:54

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=cloudinary.models.CloudinaryField(
                blank=True, default='placeholder', max_length=255, null=True, verbose_name='image'),
        ),
    ]
