# Generated by Django 5.1.2 on 2024-10-28 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0002_hotel_description_en_hotel_description_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='address_en',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='address_ru',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='city_en',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='city_ru',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='country_en',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='country_ru',
            field=models.CharField(max_length=32, null=True),
        ),
    ]