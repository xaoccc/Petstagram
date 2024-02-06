from django.db import models

from petstagram.photos.models import Photo


class PhotoReact(models.Model):
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)

    class Meta:
        abstract = True


# Create your models here.
class PhotoComment(PhotoReact):
    text = models.TextField(max_length=300)
    date_time_of_publication = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_time_of_publication']

class PhotoLike(PhotoReact):
    pass
