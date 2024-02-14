from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=30)
    pet_photo = models.URLField()
    birthdate = models.DateField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=False, editable=False)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.pk}")

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

