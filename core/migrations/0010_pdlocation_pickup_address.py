# Generated by Django 4.0 on 2024-03-14 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_customusers_vehicle_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdlocation',
            name='pickup_address',
            field=models.TextField(default=str),
            preserve_default=False,
        ),
    ]
