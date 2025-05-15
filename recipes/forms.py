from django import forms
from django.forms import inlineformset_factory
from .models import Recipe, Ingredient, Instruction

class RecipeForm(forms.ModelForm):
    """ Form to create a recipe instance in the database. """
    class Meta:
        model = Recipe
        fields = [
            'recipe_name',
            'description',
            'cooking_duration',
            'image',
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'cooking_duration': forms.Select(),
        }

class IngredientForm(forms.ModelForm):
    """ Form to add the ingredients to a recipe entry. """
    class Meta:
        model = Ingredient
        fields = [
            'name',
            'quantity',
            'unit_of_measurement',
        ]

class InstructionForm(forms.ModelForm):
    """ Form to add instructions to a recipe entry. """
    class Meta:
        model = Instruction
        fields = ['step']

# Use inlineformat to handle the ingredients and instructions in the form.
IngredientFormSet = inlineformset_factory(
    Recipe, Ingredient, form = IngredientForm, extra = 0, can_delete=True
)

InstructionFormSet = inlineformset_factory(
    Recipe, Instruction, form = InstructionForm, extra=0, can_delete=True
)