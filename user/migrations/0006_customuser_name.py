# Generated by Django 5.0.3 on 2024-03-12 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_customuser_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
