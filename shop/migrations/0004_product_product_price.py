# Generated by Django 3.0.6 on 2020-06-09 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_product_product_flavour'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_price',
            field=models.IntegerField(default=0),
        ),
    ]