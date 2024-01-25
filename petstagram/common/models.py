from django.db import models

from petstagram.photos.models import Photo


class PhotoReact(models.Model):
    to_photo = models.ForeignKey(Photo, on_delete=models.DO_NOTHING)

    class Meta:
        abstract = True


# Create your models here.
class PhotoComment(PhotoReact):
    text = models.TextField(max_length=300)
    date_time_of_publication = models.DateTimeField(auto_now_add=True)

class PhotoLike(PhotoReact):
    pass
