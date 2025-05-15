from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='user_profile'),
    path('create_profile/', views.create_profile, name='create_profile'),
    path('edit/', views.edit_profile, name='edit_profile'),
]