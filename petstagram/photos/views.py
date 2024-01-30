from django.shortcuts import render, redirect

from petstagram.photos.models import Photo


# Create your views here.
def add_photo(request):
    return render(request, 'photos/photo-add-page.html')

def show_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    likes = photo.photolike_set.all()
    comments = photo.photocomment_set.all()

    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments
    }

    return render(request, 'photos/photo-details-page.html', context)

def edit_photo(request, pk):
    return render(request, 'photos/photo-edit-page.html')

def delete_photo(request, pk):
    Photo.objects.get(pk=pk).delete()
    return redirect('home-page')

