# Generated by Django 5.0.3 on 2024-03-30 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_alter_customuser_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='description',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]
