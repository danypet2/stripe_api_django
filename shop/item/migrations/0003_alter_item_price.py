# Generated by Django 5.0 on 2023-12-06 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_item_description_item_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.IntegerField(),
        ),
    ]
