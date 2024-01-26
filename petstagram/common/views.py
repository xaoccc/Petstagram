from django.shortcuts import render, redirect

from petstagram.common.models import PhotoLike
from petstagram.photos.models import Photo


def home_page(request):
    all_photos = Photo.objects.all()

    context = {
        'all_photos': all_photos
    }

    return render(request, 'common/home-page.html', context)

def error_404(request):
    return render(request, '404.html')


def like_functionality(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    liked_object = PhotoLike.objects.filter(to_photo_id=photo_id)

    if liked_object:
        liked_object.delete()
    else:
        like = PhotoLike(to_photo=photo)
        like.save()


    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')
