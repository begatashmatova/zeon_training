# Generated by Django 4.0.5 on 2022-06-14 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0028_product_hits_product_novelty'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='item',
            field=models.CharField(blank=True, db_column='item', max_length=100),
        ),
    ]
