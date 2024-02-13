from django.urls import path

from petstagram.common import views

urlpatterns = (
    path('', views.HomePageView.as_view(), name='home-page'),
    path('404/', views.error_404, name='error_404'),
    path('like/<int:photo_id>/', views.like_functionality, name='like'),
    path('share/<int:photo_id>/', views.copy_link_to_clipboard, name='share'),
    path('comment/<int:photo_id>/', views.add_comment, name='comment'),
)