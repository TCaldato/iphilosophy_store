# Generated by Django 3.2.23 on 2024-04-03 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
