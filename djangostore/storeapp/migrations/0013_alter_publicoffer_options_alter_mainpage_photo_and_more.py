# Generated by Django 4.0.5 on 2022-06-13 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0012_alter_collection_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publicoffer',
            options={'verbose_name': 'Publicoffer', 'verbose_name_plural': 'Public offers'},
        ),
        migrations.AlterField(
            model_name='mainpage',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='news',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo1',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo2',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo3',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]