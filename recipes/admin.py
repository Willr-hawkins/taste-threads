from django.contrib import admin
from .models import Recipe
from django import forms

# Register your models here.
class RecipeAdminForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

class RecipeAdmin(admin.ModelAdmin):
    form = RecipeAdminForm

admin.site.register(Recipe, RecipeAdmin)