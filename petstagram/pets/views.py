from django.shortcuts import render

# Create your views here.
def add_pet(request):
    return render(request, 'pets/pet-add-page.html')

def show_pet(request, pet_slug):
    return render(request, 'pets/pet-details-page.html')

def edit_pet(request, pet_slug):
    return render(request, 'pets/pet-edit-page.html')

def delete_pet(request, pet_slug):
    return render(request, 'pets/pet-delete-page.html')