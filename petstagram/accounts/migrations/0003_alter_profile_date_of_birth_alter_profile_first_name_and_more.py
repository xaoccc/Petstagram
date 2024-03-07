# Generated by Django 4.2.10 on 2024-03-07 09:28

import django.core.validators
from django.db import migrations, models
import petstagram.accounts.validators


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, validators=[petstagram.accounts.validators.date_of_birth_validator]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.MinLengthValidator(2, 'First name must be at least two characters long'), petstagram.accounts.validators.name_validator]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.MinLengthValidator(2, 'Last name must be at least two characters long'), petstagram.accounts.validators.name_validator]),
        ),
    ]
