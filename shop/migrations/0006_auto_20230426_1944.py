# Generated by Django 3.2.18 on 2023-04-26 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20230419_1136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='type',
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.DeleteModel(
            name='Brand',
        ),
    ]
