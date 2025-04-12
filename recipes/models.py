from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import default_storage
from storages.backends.s3boto3 import S3Boto3Storage

# Define time choices for the cooking duration.
COOKING_TIME_CHOICES = [(i, f"{i} mins") for i in range(5, 181, 5)]

class Ingredient(models.Model):
    """ Create a database entry for an ingredient for a recipe. """
    name = models.CharField(max_length=255)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit_of_measurement = models.CharField(max_length=50, choices=[('grams', 'grams'), ('ml', 'milliliters'), ('cup', 'cups'), ('tbsp', 'tablespoons'), ('tsp', 'teaspoons'), ('Oz', 'ounces')])

    def __str__(self):
        return f"{self.quantity} {self.unit_of_measurement} of {self.name}"

class Recipe(models.Model):
    """Create a database entry for a recipe."""
    chef = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chef')
    recipe_name = models.CharField(max_length=256)
    description = models.TextField()
    ingredients = models.ManyToManyField(Ingredient)
    instructions = models.TextField()
    cooking_duration = models.PositiveIntegerField(
        choices=COOKING_TIME_CHOICES,
        help_text='Cooking time in minutes',
    )
    image = models.ImageField(upload_to='recipes/', storage=S3Boto3Storage(), null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.recipe_name