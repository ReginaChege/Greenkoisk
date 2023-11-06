# Generated by Django 3.2.12 on 2023-07-14 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_product_vendor'),
        ('product_cart', '0002_product_cart_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_cart',
            name='products',
            field=models.ManyToManyField(to='inventory.Product'),
        ),
    ]
