from django.db import models
from django.contrib.auth.models import User
from storages.backends.s3boto3 import S3Boto3Storage

from django_countries.fields import CountryField

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='recipes/', storage=S3Boto3Storage(), null=True, blank=True)
    bio = models.TextField()
    country = CountryField(blank_label='Country *', null=True, blank=True)

    def __str__(self):
        return self.user.username