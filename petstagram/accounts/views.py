from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from petstagram.accounts.forms import CustomUserCreationForm, ProfileEditForm
from petstagram.accounts.models import Profile
from petstagram.common.models import PhotoLike
from petstagram.pets.models import Pet
from petstagram.photos.models import Photo
from django.contrib.auth.views import LogoutView

UserModel = get_user_model()


class LoginProfileView(LoginView):
    authentication_form = AuthenticationForm
    template_name = 'accounts/login-page.html'


class LogoutProfileView(LogoutView):
    pass


class CreateProfileView(CreateView):
    model = UserModel
    form_class = CustomUserCreationForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('home-page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'].fields['email'].widget.attrs['placeholder'] = 'Email'
        context['form'].fields['password1'].widget.attrs['placeholder'] = 'Password'
        context['form'].fields['password2'].widget.attrs['placeholder'] = 'Repeat Password'
        return context





class DetailProfileView(DetailView, ListView):
    model = Profile
    template_name = 'accounts/profile-details-page.html'
    context_object_name = 'owner'
    query_pk_and_slug = True
    object_list = Pet.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pets = Pet.objects.filter(owner=self.object.user)
        photos = Photo.objects.filter(tagged_pets__in=pets).distinct('id')
        context['own_pets'] = pets
        context['pets_count'] = pets.count()
        context['photos'] = photos
        context['photos_count'] = photos.count()
        context['photo_likes'] = PhotoLike.objects.filter(to_photo__in=photos).count()

        return context

class EditProfileView(UpdateView):
    model = Profile
    template_name = 'accounts/profile-edit-page.html'
    form_class = ProfileEditForm

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_success_url(self):
        return reverse_lazy('profile-show', kwargs={'pk': self.object.pk})


class DeleteProfileView(DeleteView):
    model = UserModel
    template_name = 'accounts/profile-delete-page.html'
    success_url = reverse_lazy('home-page')



