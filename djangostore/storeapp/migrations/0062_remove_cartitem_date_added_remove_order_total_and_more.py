# Generated by Django 4.0.5 on 2022-06-28 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0061_remove_cartitem_order_hist_cartitem_cart_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='order',
            name='total',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='old_price',
            field=models.IntegerField(blank=True, db_column='old_price', default=0),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='size',
            field=models.CharField(blank=True, db_column='size', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='old_price',
            field=models.IntegerField(blank=True, db_column='old_price', default=0),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orderitems', to='storeapp.order'),
        ),
        migrations.AlterField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='carts', to='storeapp.cart'),
        ),
    ]
