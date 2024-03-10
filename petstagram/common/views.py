from django.shortcuts import render, redirect, resolve_url
from django.views.generic import ListView

from petstagram.accounts.models import Profile
from petstagram.common.models import PhotoLike
from petstagram.photos.models import Photo
from petstagram.common.forms import CommentForm
from pyperclip import copy


class HomePageView(ListView):
    model = Photo
    template_name = 'common/home-page.html'
    context_object_name = 'all_photos'
    paginate_by = 1

    def request_pet_name(self, get_name):
        if get_name:
            return f'&pet_name={get_name}'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        if Profile.objects.filter(pk=self.request.user.pk):
            context['profile'] = Profile.objects.get(pk=self.request.user.pk)
        pet_name_pattern = self.request.GET.get("pet_name", None)

        current_photo_id = self.request.session.get('current_photo_id')

        context['current_user_current_photo_likes'] = PhotoLike.objects.filter(user_liked_id=self.request.user.id, to_photo=current_photo_id)
        if pet_name_pattern:
            context['request_pet_name'] = self.request_pet_name(pet_name_pattern)
        else:
            context['request_pet_name'] = ""

        return context

    def get_queryset(self):
        queryset = Photo.objects.all()
        pet_name_pattern = self.request.GET.get("pet_name", None)

        if pet_name_pattern:
            self.request.session["pet_name"] = pet_name_pattern

        else:
            self.request.session.pop("pet_name", None)

        pet_name_session = self.request.session.get("pet_name")

        if pet_name_pattern:
            queryset = queryset.filter(tagged_pets__name__icontains=pet_name_session)
        return queryset

def error_404(request):
    return render(request, '404.html')


def like_functionality(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    user = request.user
    liked_object = PhotoLike.objects.filter(to_photo_id=photo_id, user_liked_id=user.id)

    if liked_object:
        liked_object.delete()
    else:
        like = PhotoLike(to_photo=photo, user_liked_id=user.id)
        like.save()

    context = {
        'all_photos': Photo.objects.all(),
        'comment_form': CommentForm(),
        'profile': Profile.objects.get(pk=request.user.pk),
        'current_user_current_photo_likes': PhotoLike.objects.filter(user_liked_id=request.user.id, to_photo=photo_id)
    }

    # return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')
    return render(request, 'common/home-page.html', context=context)


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


