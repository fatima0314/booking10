# Generated by Django 5.1.2 on 2024-10-27 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='hotel_name_en',
            field=models.CharField(max_length=36, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='hotel_name_ru',
            field=models.CharField(max_length=36, null=True),
        ),
    ]