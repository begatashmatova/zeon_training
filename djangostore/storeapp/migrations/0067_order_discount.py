# Generated by Django 4.0.5 on 2022-06-28 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0066_order_items_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='discount',
            field=models.IntegerField(blank=True, db_column='discount', default=0),
        ),
    ]