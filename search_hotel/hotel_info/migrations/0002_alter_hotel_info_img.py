# Generated by Django 4.1.4 on 2022-12-27 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_info', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel_info',
            name='img',
            field=models.FileField(upload_to='media'),
        ),
    ]
