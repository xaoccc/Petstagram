from django.shortcuts import render

from petstagram.pets.models import Pet
from petstagram.photos.models import Photo


# Create your views here.
def add_pet(request):
    return render(request, 'pets/pet-add-page.html')

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