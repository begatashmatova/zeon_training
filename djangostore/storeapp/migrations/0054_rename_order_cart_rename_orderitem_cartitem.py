# Generated by Django 4.0.5 on 2022-06-24 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0053_remove_order_color_remove_order_photo_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Order',
            new_name='Cart',
        ),
        migrations.RenameModel(
            old_name='OrderItem',
            new_name='CartItem',
        ),
    ]