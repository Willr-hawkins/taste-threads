from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory

from .models import Recipe, Ingredient, Instruction
from .forms import RecipeForm, IngredientForm, InstructionForm, IngredientFormSet, InstructionFormSet

@login_required
def create_recipe(request):
    IngredientFormSet = modelformset_factory(Ingredient, form=IngredientForm, extra=1)
    InstructionFormSet = modelformset_factory(Instruction, form=InstructionForm, extra=1)

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        ingredient_formset = IngredientFormSet(request.POST, prefix='ingredient')
        instruction_formset = InstructionFormSet(request.POST, prefix='instruction')

        if form.is_valid() and ingredient_formset.is_valid() and instruction_formset.is_valid():
            recipe = form.save(commit=False)
            recipe.chef = request.user
            recipe.save()

            for ingredient in ingredient_formset:
                obj = ingredient.save(commit=False)
                obj.recipe = recipe
                obj.save()

            for instruction in instruction_formset:
                obj = instruction.save(commit=False)
                obj.recipe = recipe
                obj.save()

            return redirect('recipe_detail', recipe_id=recipe.pk)
    else:
        form = RecipeForm()
        ingredient_formset = IngredientFormSet(queryset=Ingredient.objects.none(), prefix='ingredient')
        instruction_formset = InstructionFormSet(queryset=Instruction.objects.none(), prefix='instruction')

    context = {
        'form': form,
        'ingredient_formset': ingredient_formset,
        'instruction_formset': instruction_formset,
    }

    return render(request, 'recipes/create_recipe.html', context)

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

