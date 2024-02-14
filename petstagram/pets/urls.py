from django.urls import path, include
from petstagram.pets.views import AddPetView, DetailsPetView, EditPetView, DeletePetView

urlpatterns = (
    path('add/', AddPetView.as_view(), name='pet-add'),
    path('<str:username>/pet/<slug:pet_slug>/', include([
        path('', DetailsPetView.as_view(), name='pet-show'),
        path('edit/', EditPetView.as_view(), name='pet-edit'),
        path('delete/', DeletePetView.as_view(), name='pet-delete'),
    ])),
)
