# Generated by Django 3.0 on 2022-07-05 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_payment_method'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='payment_method',
        ),
    ]