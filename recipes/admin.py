from django.contrib import admin
from .models import Recipe, Ingredient

# Register your models here.
class IngredientInline(admin.StackedInline):
    model = Ingredient
    extra = 1

class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientInline]

admin.site.register(Recipe, RecipeAdmin)