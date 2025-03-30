#Importing necessary libraries
from django.db import models
from django.contrib.auth.models import AbstractUser

# Creating a custom user model which extends Django's AbstractUser 
class CustomUser(AbstractUser):
    #Adding bio and profile picture as the extended fields
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile/pics', blank=True, null=True)