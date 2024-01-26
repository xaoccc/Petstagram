from django.urls import path

from petstagram.common import views

urlpatterns = (
    path('', views.home_page, name='home-page'),
    path('404/', views.error_404, name='error_404')
)