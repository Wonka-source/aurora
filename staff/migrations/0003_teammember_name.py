# Generated by Django 3.2.18 on 2023-04-30 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_teammember_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
    ]
