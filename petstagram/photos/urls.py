from django.urls import path
from petstagram.photos import views

urlpatterns = [
    path('add/', views.add, name='add'),
    path('<int:pk>/', views.details, name='details'),
    path('<int:pk>/edit/', views.edit, name='edit')
]