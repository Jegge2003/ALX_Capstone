#Importing necessary libraries
from django.db import models #For building models which map to database tables
from django.contrib.auth.models import AbstractUser

# Creating a custom user model which extends Django's AbstractUser 
class CustomUser(AbstractUser):
    """
    Here we are building the CustomUser model which will be more like a user table inheriting all default fields of Django's AbstractUser.
    It will also have in addition bio and profile picture fields.
    """
    #Adding bio and profile picture as the extended fields
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile/pics', blank=True, null=True)