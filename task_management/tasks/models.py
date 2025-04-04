#Importing necessary libraries
from django.db import models #Needed to define the database schema using python classes
from accounts.models import CustomUser #Importing the CustomUser model from the accounts app
from django.utils import timezone #To get the current time

# Create your models here.
class Task(models.Model):
    """
    Defines a new model (database table) named Task
    """
    #Allowed values for the status field
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    #Allowed values for the priority field
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True) #Field linking each task to a user
    title = models.CharField(max_length=255, null=True, blank=True) #Field storing the title of tasks
    description = models.TextField(null=True, blank=True) #Field for storing more detailed description of the task
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending') #A dropdown/select field that must be one of the status choices
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='Medium') #A dropdown/select field that must be one of the priority choices
    due_date = models.DateField(null=True, blank=True) #A date only field for task deadlines
    created_at = models.DateTimeField(default=timezone.now) #Field to automatically store the timestamp when the task is created
    updated_at = models.DateTimeField(auto_now=True) #Field to automatically store the timestamp everytime the task is edited

    #To show the task's title
    def __str__(self):
        return self.title
    
