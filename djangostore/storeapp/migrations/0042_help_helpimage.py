# Generated by Django 4.0.5 on 2022-06-17 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0041_productimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Help',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(blank=True, db_column='quesion', max_length=100)),
                ('answer', models.CharField(blank=True, db_column='answer', max_length=100)),
            ],
            options={
                'verbose_name': 'Help',
                'verbose_name_plural': 'Help',
                'db_table': 'help',
            },
        ),
        migrations.CreateModel(
            name='HelpImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
            options={
                'verbose_name': 'HelpImage',
                'verbose_name_plural': 'HelpImage',
                'db_table': 'helpimage',
            },
        ),
    ]
