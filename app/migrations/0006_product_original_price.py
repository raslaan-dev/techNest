# Generated by Django 5.1.4 on 2025-01-03 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_category_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='original_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
