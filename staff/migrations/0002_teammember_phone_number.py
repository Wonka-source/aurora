# Generated by Django 3.2.18 on 2023-04-26 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
