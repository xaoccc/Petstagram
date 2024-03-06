# Generated by Django 4.2.11 on 2024-03-05 13:03

import django.core.validators
from django.db import migrations, models
import petstagram.photos.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='pet_photos/', validators=[petstagram.photos.models.MaxFileSizeValidator(limit_value=5242880)])),
                ('description', models.TextField(blank=True, max_length=300, null=True, validators=[django.core.validators.MinLengthValidator(10)])),
                ('location', models.CharField(blank=True, max_length=30, null=True)),
                ('publication_date', models.DateField(auto_now=True)),
                ('tagged_pets', models.ManyToManyField(blank=True, related_name='photo_pet', to='pets.pet')),
            ],
        ),
    ]
