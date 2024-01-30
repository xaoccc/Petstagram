from django.shortcuts import render, redirect

from petstagram.pets.models import Pet
from petstagram.pets.forms import PetForm


# Create your views here.
def add_pet(request):
    form = PetForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('home-page')


    context = {
        'form': form
    }

    return render(request, 'pets/pet-add-page.html', context)

def show_pet(request, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.photo_set.all()

    context = {
        'pet': pet,
        'all_photos': all_photos
    }

    return render(request, 'pets/pet-details-page.html', context)

def edit_pet(request, pet_slug):
    return render(request, 'pets/pet-edit-page.html')

def delete_pet(request, pet_slug):
    return render(request, 'pets/pet-delete-page.html')