from django.urls import path
from petstagram.photos import views

urlpatterns = [
    path('add/', views.add_photo, name='photo-add'),
    path('<int:pk>/', views.show_photo, name='photo-details'),
    path('<int:pk>/edit/', views.edit_photo, name='photo-edit'),
    path('<int:pk>/delete/', views.delete_photo, name='photo-delete'),
]