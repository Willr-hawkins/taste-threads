from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm
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

@login_required
def edit_profile(request):
    """ Allow users to update their proifle information after intitail creation. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
        form = UserProfileForm(instance=profile)

    context = {
        'form': form,
    }
    return render(request, 'profiles/edit_profile.html', context)
