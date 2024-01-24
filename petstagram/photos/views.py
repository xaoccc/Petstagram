from django.shortcuts import render

# Create your views here.
def add(request):
    return render(request, 'add')

def details(request, pk):
    return render(request, 'details')

def edit(request, pk):
    return render(request, 'edit')

