from django.core.validators import BaseValidator, MinLengthValidator
from django.db import models

from petstagram.pets.models import Pet


class MaxFileSizeValidator(BaseValidator):
    def clean(self, x):
        return x.size

    def compare(self, file_size, max_size):
        return file_size > max_size

# Create your models here.
class Photo(models.Model):
    photo = models.ImageField(upload_to='pet_photos/', validators=(MaxFileSizeValidator(limit_value=5 * 1024 * 1024),))
    description = models.TextField(max_length=300, validators=(MinLengthValidator(10),), blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    tagged_pets = models.ManyToManyField(Pet, blank=True, related_name="photo_pet")
    publication_date = models.DateField(auto_now=True)



