# Generated by Django 3.1.7 on 2021-03-24 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0002_order_total_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_quantity',
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.CharField(max_length=50),
        ),
    ]
