# Generated by Django 4.0.5 on 2022-06-20 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0043_call'),
    ]

    operations = [
        migrations.AddField(
            model_name='call',
            name='call_date',
            field=models.DateTimeField(blank=True, db_column='call_date', null=True),
        ),
    ]
