from .models import UserProfile

def profile_status(request):
    """
    Adds `has_profile` = True/False to every RequestContext.
    """
    user = request.user
    if user.is_authenticated:
        has_profile = UserProfile.objects.filter(user=user).exists()
    else:
        has_profile = False
    return {
        'has_profile': has_profile
    }