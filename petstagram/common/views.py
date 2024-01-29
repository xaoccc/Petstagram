from django.shortcuts import render, redirect, resolve_url
from petstagram.common.models import PhotoLike
from petstagram.photos.models import Photo
from pyperclip import copy


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

def copy_link_to_clipboard(request, photo_id):
    copy(request.META['HTTP_HOST'] + resolve_url('photo-details', photo_id))
    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


