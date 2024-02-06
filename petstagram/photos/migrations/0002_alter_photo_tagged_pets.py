# Generated by Django 4.2.9 on 2024-02-06 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0003_rename_photo_pet_pet_photo'),
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='tagged_pets',
            field=models.ManyToManyField(blank=True, related_name='photo_pet', to='pets.pet'),
        ),
    ]
