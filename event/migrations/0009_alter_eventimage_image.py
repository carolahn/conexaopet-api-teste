# Generated by Django 5.0.3 on 2024-03-26 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0008_event_pets_ids'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventimage',
            name='image',
            field=models.ImageField(upload_to='media/event_images/'),
        ),
    ]
