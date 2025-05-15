from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('create_recipe/', views.create_recipe, name='create_recipe'),
    path('<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('edit_recipe/<int:pk>/', views.edit_recipe, name='edit_recipe'),
    path('delete_recipe/<int:pk>/', views.delete_recipe, name='delete_recipe'),
]