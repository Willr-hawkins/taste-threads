from django.shortcuts import render
from .models import Recipe
from django.conf import settings

def recipe_list(request):
    recipes = Recipe.objects.all().order_by('-date')  # Fetch all recipes, latest first
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes, 'MEDIA_URL': settings.MEDIA_URL})