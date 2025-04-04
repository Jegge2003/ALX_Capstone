from rest_framework import generics #For access to generic views like CreateAPIView and GenericAPIView
from .serializers import RegisterSerializer, LoginSerializer #Serializers for user registration and login
from rest_framework.authtoken.models import Token #Needed for login and token generation
from rest_framework.response import Response #Required for all views that return data
from rest_framework.permissions import AllowAny #Allows any user, even unauthenticated ones to access the endpoint
from rest_framework.authtoken.views import ObtainAuthToken #For generating a token when a user logs in 

# Create your views here.
class RegisterView(generics.CreateAPIView):
    """
    This view handles user registration/signup and makes it possible for even unauthenticated users to register.
    """
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class LoginView(generics.GenericAPIView):
    """
    Custom login endpoint. Handles login and gives a token if credentials are valid
    """
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        user = self.get_serializer(data=request.data).validate(request.data) #Running validation to ensure crediatials are correct
        token, created = Token.objects.get_or_create(user=user) #Gives the user a token
        return Response({'token': token.key})
    
class CustomAuthToken(ObtainAuthToken):
    """
    Provides a more detailed token response.
    """
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'user_id': token.user_id, 'username': token.user.username})