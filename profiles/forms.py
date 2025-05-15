from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from django_countries.widgets import CountrySelectWidget


class UserProfileForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True)

    class Meta:
        model = UserProfile
        fields = ['profile_image', 'bio', 'country']
        widgets = {
            'country': CountrySelectWidget(),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
    
    def save(self, commit=True):
        profile = super().save(commit=False)

        if self.user:
            self.user.username = self.cleaned_data['username']
            if commit:
                self.user.save()
            profile.user = self.user
        
        if commit:
            profile.save()
        return profile