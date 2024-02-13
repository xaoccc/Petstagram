from django.urls import path, include

from petstagram.accounts import views

urlpatterns = (
    path('register/', views.register_profile, name='profile-register'),
    path('login/', views.LoginProfileView.as_view(), name='profile-login'),
    path('logout/', views.logout_profile, name='profile-logout'),
    path('profile/<int:pk>/', include([
        path('', views.DetailProfileView.as_view(), name='profile-show'),
        path('edit/', views.edit_profile, name='profile-edit'),
        path('delete/', views.delete_profile, name='profile-delete'),
        ])
    ),
)
