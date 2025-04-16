from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import default_storage
from storages.backends.s3boto3 import S3Boto3Storage
from decimal import Decimal

# Define time choices for the cooking duration.
COOKING_TIME_CHOICES = [(i, f"{i} mins") for i in range(5, 181, 5)]

class Ingredient(models.Model):
    """A single ingredient tied to a specific recipe."""
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, related_name='ingredients')
    name = models.CharField(max_length=255)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit_of_measurement = models.CharField(
        max_length=50,
        choices=[
            ('g', 'grams'),
            ('ml', 'milliliters'),
            ('cup', 'cups'),
            ('tbsp', 'tablespoons'),
            ('tsp', 'teaspoons'),
            ('oz', 'ounces'),
            ('large', 'large'),
            ('small', 'small'),
        ]
    )

    def formatted_quantity(self):
        """Return quantity without trailing .00 if whole number."""
        if self.quantity == self.quantity.to_integral():
            return int(self.quantity)
        return self.quantity

    def display_unit(self):
        """Return the unit, singular if quantity is 1."""
        quantity = float(self.formatted_quantity())
        singulars = {
            'cups': 'cup',
            'tablespoons': 'tablespoon',
            'teaspoons': 'teaspoon',
            'grams': 'gram',
            'milliliters': 'milliliter',
            'ounces': 'ounce',
            'large': 'large',
            'small': 'small',
        }

        unit_display = dict(self._meta.get_field('unit_of_measurement').choices).get(self.unit_of_measurement, '')

        if quantity == 1:
            return singulars.get(unit_display, unit_display)
        return unit_display

    def __str__(self):
        return f"{self.formatted_quantity()} {self.display_unit()} of {self.name}"


class Instruction(models.Model):
    """ Create a recipe instruction step. Add step by step seperatly. steps tied to specifc recipe. """
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, related_name='instruction_steps')
    step = models.TextField()

class Recipe(models.Model):
    """Create a database entry for a recipe."""
    chef = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chef')
    recipe_name = models.CharField(max_length=256)
    description = models.TextField()
    cooking_duration = models.PositiveIntegerField(
        choices=COOKING_TIME_CHOICES,
        help_text='Cooking time in minutes',
    )
    image = models.ImageField(upload_to='recipes/', storage=S3Boto3Storage(), null=True, blank=True)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.recipe_name