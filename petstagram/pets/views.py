from django.shortcuts import render, redirect

from petstagram.pets.models import Pet
from petstagram.pets.forms import PetForm, PetDeleteForm


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
    pet = Pet.objects.get(slug=pet_slug)

    if request.method == "GET":
        form = PetForm(instance=pet, initial=pet.__dict__)

    else:
        form = PetForm(request.POST, instance=pet)

        if form.is_valid():
            form.save()
            return redirect('pet-show', pet_slug)

    context = {
        'form': form
    }
    return render(request, 'pets/pet-edit-page.html', context)


def delete_pet(request, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)

    if request.method == "POST":
        pet.delete()
        return redirect('home-page')

    form = PetDeleteForm(initial=pet.__dict__)

    context = {
        'form': form
    }
    return render(request, 'pets/pet-delete-page.html', context)
