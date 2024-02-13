from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView

from petstagram.pets.models import Pet
from petstagram.photos.models import Photo


def register_profile(request):
    return render(request, 'accounts/register-page.html')


class LoginProfileView(LoginView):
    authentication_form = AuthenticationForm
    template_name = 'accounts/login-page.html'
    success_url = reverse_lazy('home-page')


def logout_profile(request):
    return redirect('home-page')

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


def show_profile(request, pk):
    owner = User.objects.filter(pk=pk)
    # own_pets should be filtered on the profile pk, therefore User and Pet should be connected models
    # For testing purpose, here pk=pk (hardcoded).
    own_pets = Pet.objects.filter(pk=2)

    context = {
        'own_pets': own_pets
    }

    return render(request, 'accounts/profile-details-page.html', context)



def edit_profile(request, pk):
    return render(request, 'accounts/profile-edit-page.html')

def delete_profile(request, pk):
    return render(request, 'accounts/profile-delete-page.html')


