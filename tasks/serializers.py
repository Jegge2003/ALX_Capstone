from rest_framework import serializers #For converting Python Objects to JSON and vice versa
from .models import Task #Importing the task model

class TaskSerializer(serializers.ModelSerializer):
    """
    For converting task model into JSON data, validating and converting incoming JSON data into a Task model
    """
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['user']