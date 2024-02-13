
from django.http import request
from django.shortcuts import render, redirect, resolve_url
from django.views.generic import ListView

from petstagram.common.models import PhotoLike
from petstagram.photos.models import Photo
from petstagram.common.forms import CommentForm
from pyperclip import copy


class HomePageView(ListView):
    model = Photo
    template_name = 'common/home-page.html'
    context_object_name = 'all_photos'
    paginate_by = 1

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context

    def get_queryset(self):
        queryset = Photo.objects.all()
        pet_name_pattern = self.request.GET.get("pet_name", None)
        if pet_name_pattern:
            queryset = queryset.filter(tagged_pets__name__icontains=pet_name_pattern)
        return queryset




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


