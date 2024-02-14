from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView
from petstagram.pets.models import Pet
from petstagram.photos.models import Photo
from django.contrib.auth.views import LogoutView

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label="Email", required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

class CustomLogoutView(LogoutView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.template_name = 'common/home-page.html'

class CreateProfileView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('home-page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'].fields['username'].widget.attrs['placeholder'] = 'Username'
        context['form'].fields['email'].widget.attrs['placeholder'] = 'Email'
        context['form'].fields['password1'].widget.attrs['placeholder'] = 'Password'
        context['form'].fields['password2'].widget.attrs['placeholder'] = 'Repeat Password'
        return context


class LoginProfileView(LoginView):
    authentication_form = AuthenticationForm
    template_name = 'accounts/login-page.html'
    success_url = reverse_lazy('home-page')


class DetailProfileView(DetailView, ListView):
    model = User
    template_name = 'accounts/profile-details-page.html'
    context_object_name = 'owner'
    query_pk_and_slug = True
    object_list = Pet.objects.filter(pk=2)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pets = Pet.objects.filter(pk__lte=2)
        photos = Photo.objects.filter(tagged_pets__in=pets)
        context['own_pets'] = pets
        context['pets_count'] = pets.count()
        context['photos'] = photos
        context['photos_count'] = photos.count()
        return context



def edit_profile(request, pk):
    return render(request, 'accounts/profile-edit-page.html')

def delete_profile(request, pk):
    return render(request, 'accounts/profile-delete-page.html')


