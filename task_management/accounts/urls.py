#Importing the necessary libraries
from django.urls import path #Used to define URL routes
from .views import RegisterView, LoginView
from .views import CustomAuthToken

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'), #Mapping the URL register to the RegisterView class
    path('login/', CustomAuthToken.as_view(), name='token_auth'), #Mapping the URL login to CustomAuthToken
]