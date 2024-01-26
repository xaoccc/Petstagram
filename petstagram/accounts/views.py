from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from petstagram.pets.models import Pet


def register_profile(request):
    return render(request, 'accounts/register-page.html')

def login_profile(request):
    return render(request, 'accounts/login-page.html')

def logout_profile(request):
    return redirect('home-page')

def show_profile(request, pk):
    owner = User.objects.filter(pk=pk)
    # own_pets should be filtered on the profile pk, therefore User and Pet should be connected models
    # For testing purpose, here pk=pk (hardcoded).
    own_pets = Pet.objects.filter(pk=pk)

    context = {
        'own_pets': own_pets
    }

    return render(request, 'accounts/profile-details-page.html', context)

def edit_profile(request, pk):
    return render(request, 'accounts/profile-edit-page.html')

def delete_profile(request, pk):
    return render(request, 'accounts/profile-delete-page.html')


