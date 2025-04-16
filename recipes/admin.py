from django.contrib import admin
from .models import Recipe, Ingredient, Instruction

# Register your models here.
class IngredientInline(admin.StackedInline):
    model = Ingredient
    extra = 1

class InstructionInline(admin.StackedInline):
    model = Instruction
    extra = 1

class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientInline, InstructionInline]

admin.site.register(Recipe, RecipeAdmin)