# accounts/urls.py

from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='user_login'),
    path('logout/', views.CustomLogoutView.as_view(), name='user_logout'),
    path('register/', views.register_view, name='user_register'),
    path('profile/', views.profile_view, name='user_profile'),
]
