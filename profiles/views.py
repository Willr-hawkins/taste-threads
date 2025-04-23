from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from recipes.models import Recipe

# Create your views here.
@login_required
def profile(request):
    """ Display a users profile with thier individual detials. """
    profile = get_object_or_404(UserProfile, user=request.user)
    recipes = Recipe.objects.filter(chef = profile.user)
    context = {
        'userprofile': profile,
        'recipes': recipes,
    }

    return render(request, 'profiles/profile.html', context)