# Generated by Django 3.2.18 on 2023-04-26 19:09

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=255)),
                ('bio', models.TextField(blank=True)),
                ('photo', cloudinary.models.CloudinaryField(default='staff_placeholder', max_length=255, verbose_name='image')),
                ('date_registered', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='team_member', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Team Members',
                'ordering': ['date_registered'],
            },
        ),
    ]