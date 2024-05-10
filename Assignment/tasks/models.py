# Import necessary modules
from django.db import models
from django.db import models
from django.contrib.auth.models import User


# Define the Task model
class Task(models.Model):
    # Define fields for the Task model
    title = models.CharField(max_length=255) # Title of the task
    description = models.TextField() # Description of the task
    completed = models.BooleanField(default=False) # Flag indicating whether the task is completed or not
    owner = models.ForeignKey(User, on_delete=models.CASCADE) # Owner of the task, linked to a User model
    labels = models.ManyToManyField(to='Label', related_name='tasks') # Labels associated with the task
  
    # Define a string representation for the Task model
    def __str__(self):
        return self.title # Return the title of the task as the string representation


# Define the Label model
class Label(models.Model):
    name = models.CharField(max_length=255, unique=True) # Name of the Label
    owner = models.ForeignKey(User, on_delete=models.CASCADE) # Owner of the label, linked to a User model
    
    # Define a string representation for the Label model
    def __str__(self):
        return self.name # Return the name of the label as the string representation


