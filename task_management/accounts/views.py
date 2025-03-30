from django.shortcuts import render
from rest_framework import generics
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

# Create your views here.
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        user = self.get_serializer(data=request.data).validate(request.data)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})