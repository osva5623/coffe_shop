# Generated by Django 5.1.2 on 2024-11-08 02:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0001_initial"),
        ("products", "0003_alter_product_date_creation"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="order_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="orderproduct",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="products.product"
            ),
        ),
    ]
