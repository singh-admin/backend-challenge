# Import necessary modules
from rest_framework import serializers
from .models import Task, Label


# Define the serializer for the Task model
class TaskSerializer(serializers.ModelSerializer):
    # Automatically set the owner to the current user
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault()) 
    # Allow labels to be optional
    labels = serializers.PrimaryKeyRelatedField(many=True, queryset=Label.objects.all(), required=False)
    class Meta:
        model = Task # serializer based on Task
        fields = '__all__'  # Serialize all fields of the Task model


# Define the serializer for the Label model
class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label # serializer based on Label
        fields = '__all__'   # Serialize all fields of the Label model
