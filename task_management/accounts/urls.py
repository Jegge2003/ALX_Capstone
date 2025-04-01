from django.urls import path
from .views import RegisterView, LoginView
from .views import CustomAuthToken

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('login/', CustomAuthToken.as_view(), name='token_auth'),
]