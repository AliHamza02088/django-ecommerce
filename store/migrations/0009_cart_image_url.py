# Generated by Django 5.1.4 on 2025-02-05 10:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_remove_features_product_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='image_url',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.productimage'),
        ),
    ]
