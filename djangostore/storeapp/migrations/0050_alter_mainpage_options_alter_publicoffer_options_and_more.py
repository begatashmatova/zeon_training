# Generated by Django 4.0.5 on 2022-06-23 12:16

import colorfield.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('storeapp', '0049_orderitem_color'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mainpage',
            options={'verbose_name': 'Главная страница', 'verbose_name_plural': 'Главная страница'},
        ),
        migrations.AlterModelOptions(
            name='publicoffer',
            options={'verbose_name': 'Публичная оферта', 'verbose_name_plural': 'Публичная оферта'},
        ),
        migrations.AddField(
            model_name='orderitem',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='color',
            field=colorfield.fields.ColorField(db_column='color', default='#FFFFFF', image_field=None, max_length=18, samples=None),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]