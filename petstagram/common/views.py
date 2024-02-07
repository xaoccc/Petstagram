from django.shortcuts import render, redirect, resolve_url

from petstagram.common.models import PhotoLike
from petstagram.photos.models import Photo
from petstagram.common.forms import CommentForm
from pyperclip import copy


def home_page(request):
    comment_form = CommentForm()
    photos = Photo.objects.all()
    pet_name_pattern = request.GET.get("pet_name", None)
    all_photos = photos if not pet_name_pattern else photos.filter(tagged_pets__name__icontains=pet_name_pattern,)

    context = {
        'all_photos': all_photos,
        'comment_form': comment_form,
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


def add_comment(request, photo_id):
    if request.method == "POST":
        photo = Photo.objects.get(id=photo_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            photocomment = form.save(commit=False)
            photocomment.to_photo = photo
            photocomment.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


