from django.shortcuts import render
from recipes.models import Recipe

def home(request):
    latest_recipes = Recipe.objects.order_by('-posted_at')[:3]
    return render(request, 'home/home_page.html', {'latest_recipes': latest_recipes})

