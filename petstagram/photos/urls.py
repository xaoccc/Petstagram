from django.urls import path
from petstagram.photos import views

urlpatterns = [
    path('add/', views.AddPhotoView.as_view(), name='photo-add'),
    path('<int:pk>/', views.PhotoDetailsView.as_view(), name='photo-details'),
    path('<int:pk>/edit/', views.PhotoEditView.as_view(), name='photo-edit'),
    path('<int:pk>/delete/', views.delete_photo, name='photo-delete'),
]