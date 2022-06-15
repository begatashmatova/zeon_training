# Generated by Django 4.0.5 on 2022-06-13 12:03

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0015_choice_col'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(blank=True, db_column='title', max_length=100)),
                ('collection', models.CharField(choices=[('Summer-2022', 'Summer-2022'), ('Winter-2022', 'Winter-2022')], max_length=256, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'db_table': 'product',
            },
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
    ]