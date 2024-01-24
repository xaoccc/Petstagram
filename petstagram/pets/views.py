from django.shortcuts import render

# Create your views here.
def add_pet(request):
    return(request, 'add_pet')

def pet_details(request):
    return(request, 'pet_details')

def edit_pet(request):
    return(request, 'edit_pet')

def delete_pet(request):
    return(request, 'delete_pet')