# Generated by Django 4.2.9 on 2024-01-30 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photocomment',
            options={'ordering': ['date_time_of_publication']},
        ),
    ]