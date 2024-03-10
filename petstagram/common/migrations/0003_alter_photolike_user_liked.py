# Generated by Django 4.2.10 on 2024-03-06 20:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0002_photolike_user_liked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photolike',
            name='user_liked',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]