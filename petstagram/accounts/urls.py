from django.urls import path, include

from petstagram.accounts import views

urlpatterns = (
    path('register/', views.CreateProfileView.as_view(), name='profile-register'),
    path('login/', views.LoginProfileView.as_view(), name='profile-login'),
    path('logout/', views.CustomLogoutView.as_view(), name='profile-logout'),
    path('profile/<int:pk>/', include([
        path('', views.DetailProfileView.as_view(), name='profile-show'),
        path('edit/', views.EditProfileView.as_view(), name='profile-edit'),
        path('delete/', views.DeleteProfileView.as_view(), name='profile-delete'),
        ])
    ),
)
