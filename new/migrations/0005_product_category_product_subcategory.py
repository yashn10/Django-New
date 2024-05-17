# Generated by Django 5.0.6 on 2024-05-14 12:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0004_rename_products_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='new.category'),
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='new.subcategory'),
        ),
    ]
