# Generated by Django 3.2.18 on 2023-04-20 03:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0008_alter_order_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user',
            new_name='user_profile',
        ),
    ]
