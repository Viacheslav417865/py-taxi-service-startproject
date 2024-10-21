# Generated by Django 5.1.2 on 2024-10-21 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0002_remove_car_drivers_remove_car_manufacturer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='license_number',
            field=models.CharField(default='default_license_number', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='manufacturer_name',
            field=models.CharField(default='default_manufacturer', max_length=100),
        ),
    ]