# Generated by Django 3.2.18 on 2023-04-26 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch_repair', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchrepair',
            name='other',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='watchrepair',
            name='priority',
            field=models.IntegerField(choices=[(0, 'Low'), (1, 'Medium'), (2, 'High')], default=1),
        ),
        migrations.AddField(
            model_name='watchrepair',
            name='staff_notes',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='watchrepair',
            name='status',
            field=models.IntegerField(choices=[(0, 'New'), (1, 'In Progress'), (2, 'Complected')], default=0),
        ),
    ]
