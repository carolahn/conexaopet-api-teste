# Generated by Django 5.0.3 on 2024-03-21 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_remove_event_pets_ids'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='pets',
            new_name='pets_ids',
        ),
    ]