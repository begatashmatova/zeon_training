# Generated by Django 4.0.5 on 2022-06-13 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0009_alter_benefit_icon_alter_collection_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='benefit',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='collection',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
