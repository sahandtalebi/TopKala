# Generated by Django 3.1.6 on 2021-02-27 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TopKala_product', '0007_remove_product_attributes'),
        ('TopKala_attributes', '0002_auto_20210224_2011'),
    ]

    operations = [
        migrations.AddField(
            model_name='productattributes',
            name='products',
            field=models.ManyToManyField(to='TopKala_product.Product'),
        ),
    ]
