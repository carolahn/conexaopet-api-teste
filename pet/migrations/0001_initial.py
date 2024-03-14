# Generated by Django 5.0.3 on 2024-03-13 01:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('age_year', models.IntegerField()),
                ('age_month', models.IntegerField()),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('size', models.CharField(choices=[('miniatura', 'Miniatura'), ('pequeno', 'Pequeno'), ('médio', 'Médio'), ('grande', 'Grande')], max_length=50)),
                ('breed', models.CharField(max_length=100)),
                ('personality', models.JSONField()),
                ('get_along', models.JSONField()),
                ('description', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PetImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pet_images/')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='pet.pet')),
            ],
        ),
    ]
