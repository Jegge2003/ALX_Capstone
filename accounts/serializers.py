from rest_framework import serializers #To help create/validate API data
from .models import CustomUser #Importing the customuser model which inherits from Django's Abstract User
from django.contrib.auth import authenticate #To check if the username and password match an existing user
from rest_framework.authtoken.models import Token

class RegisterSerializer(serializers.ModelSerializer):
    """
    This is the serializer for handling user input (JSON) into a CustomUser object in the database
    """
    class Meta:
        model = CustomUser
        fields = ['username', 'password'] #The only required fields from the user
        extra_kwargs = {'password': {'write_only': True}} #Don't show password when returning user data

    def create(self, validated_data):
        """
        This gets triggered when someone sends a post request to register
        """
        try:
            user = CustomUser.objects.create_user(**validated_data)
            Token.objects.create(user=user) #Creates unique token tied to the user for logging in later
            return user
        except Exception as e:
            raise serializers.ValidationError({"detail": str(e)})
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        """
        Checks the provided username and password and if it matches, the user object is returned.
        If data doesn't match, raises an error.
        """
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid credentials.")