from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('create_recipe/', views.create_recipe, name='create_recipe'),
    path('recipes/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
]