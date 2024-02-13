from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from petstagram.common.forms import CommentForm
from petstagram.pets.models import Pet
from petstagram.pets.forms import PetCreateForm, PetEditForm, PetDeleteForm


class AddPetView(CreateView):
    model = Pet
    template_name = 'pets/pet-add-page.html'
    form_class = PetCreateForm
    success_url = reverse_lazy('home-page')


def show_pet(request, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.photo_pet.all()
    comment_form = CommentForm()

    context = {
        'pet': pet,
        'all_photos': all_photos,
        'comment_form': comment_form
    }

    return render(request, 'pets/pet-details-page.html', context)

def edit_pet(request, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)

    form = PetEditForm(request.POST or None, instance=pet)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('pet-show', pet_slug)

    context = {
        'form': form,
        'pet': pet
    }
    return render(request, 'pets/pet-edit-page.html', context)


def delete_pet(request, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)

    form = PetDeleteForm(request.POST or None, instance=pet)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('home-page')

    context = {
        'form': form,
        'pet': pet
    }
    return render(request, 'pets/pet-delete-page.html', context)


