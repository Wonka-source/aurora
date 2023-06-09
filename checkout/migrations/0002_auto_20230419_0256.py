# Generated by Django 3.2.18 on 2023-04-19 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='billing_address1',
            field=models.CharField(max_length=89, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_cost',
            field=models.DecimalField(
                decimal_places=2, default=0, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_method',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='full_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='grand_total',
            field=models.DecimalField(
                decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_total',
            field=models.DecimalField(
                decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_address1',
            field=models.CharField(max_length=89, null=True),
        ),
    ]
