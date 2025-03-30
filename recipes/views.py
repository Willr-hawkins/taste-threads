from django.shortcuts import render
from .models import Recipe

def recipe_list(request):
    recipes = Recipe.objects.all().order_by('-date')  # Fetch all recipes, latest first
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})