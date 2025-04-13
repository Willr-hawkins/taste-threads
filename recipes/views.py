from django.shortcuts import render, get_object_or_404
from django.conf import settings

from .models import Recipe

def recipe_list(request):
    """ A view to show a list of all recipes on the site. """
    recipes = Recipe.objects.all().order_by('-posted_at')  # Fetch all recipes, latest first
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes, 'MEDIA_URL': settings.MEDIA_URL})

def recipe_detail(request, recipe_id):
    """ A view to show the an individual recipes details page. """
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    context = {
        'recipe': recipe,
    }

    return render(request, 'recipes/recipe_detail.html', context)