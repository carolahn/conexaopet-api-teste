# Generated by Django 5.0.3 on 2024-03-19 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0002_pet_followers'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='pet',
            table='pet',
        ),
        migrations.AlterModelTable(
            name='petimage',
            table='pet_image',
        ),
    ]