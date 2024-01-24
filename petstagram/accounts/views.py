from django.shortcuts import render

def register(request):
    return render(request, 'register')

def login(request):
    return render(request, 'login')

def show_profile_details(request):
    return render(request, 'profile-details')

def edit_profile(request):
    return render(request, 'profile-edit')

def delete_profile(request):
    return render(request, 'profile-delete')


