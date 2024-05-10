# Import necessary modules
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Task, Label
from rest_framework import generics
from .serializers import TaskSerializer, LabelSerializer
from rest_framework.authtoken.views import obtain_auth_token



# Define a view for obtaining authentication tokens
obtain_auth_token_view = obtain_auth_token

# View for handling tasks
class TaskView(APIView):
    permission_classes = [IsAuthenticated] # Ensure that the user is authenticated
    
    # Handle POST request to create a new task
    def post(self, request):
        user = request.user # Get the authenticated user
        serializer = TaskSerializer(data=request.data, context={'request': request}) # Deserialize request data into a Task object
        if serializer.is_valid():
            serializer.save(owner=user) # Set the owner of the task to the authenticated user
            return Response(serializer.data, status=status.HTTP_201_CREATED) # Return the serialized task data with 201 status code for successful creation
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # Return errors if serializer is not valid
    
    # Handle GET request to retrieve tasks belonging to the user
    def get(self, request):
        user = request.user # Get the authenticated user
        tasks = Task.objects.filter(owner=user) # Retrieve tasks associated with the authenticated user
        serializer = TaskSerializer(tasks, many=True) # Serialize tasks data
        return Response(serializer.data) # Return serialized tasks data
    
    # Handle PUT request to update an existing task
    def put(self, request, pk):
        user = request.user  # Get the authenticated user
        try:
            # Retrieve the task with the specified primary key and owned by the authenticated user
            task = Task.objects.get(pk=pk, owner=user) 
        except Task.DoesNotExist:
            # Return error if task not found
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
        # Deserialize request data into the existing task object
        serializer = TaskSerializer(task, data=request.data, context={'request': request}) 
        if serializer.is_valid():
            serializer.save() # Save the updated task
            return Response(serializer.data) # Return serialized task data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # Return errors if serializer is not valid
    
    # Handle DELETE request to delete an existing task
    def delete(self, request, pk):
        user = request.user # Get the authenticated user
        try:
            # Retrieve the task with the specified primary key and owned by the authenticated user
            task = Task.objects.get(pk=pk, owner=user)
        except Task.DoesNotExist:
            # Return error if task not found
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
        task.delete() # Delete the task
        return Response({'message': 'Task deleted successfully'}, status=status.HTTP_200_OK) # Return 200 status code for successful deletion


# View for handling label
class LabelView(APIView):
    permission_classes = [IsAuthenticated] # Ensure that the user is authenticated
    
    # Handle POST request to create a new label
    def post(self, request):
        user = request.user # Get the authenticated user
        serializer = LabelSerializer(data=request.data) # Deserialize request data into a Label object
        if serializer.is_valid():
            serializer.save(owner=user) # Set the owner of the label to the authenticated user
            # Return the serialized label data with 201 status code for successful creation
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # Return errors if serializer is not valid
    
    # Handle GET request to retrieve labels belonging to the user
    def get(self, request):
        user = request.user # Get the authenticated user
        labels = Label.objects.filter(owner=user) # Retrieve labels associated with the authenticated user
        serializer = LabelSerializer(labels, many=True) # Serialize labels data
        return Response(serializer.data) # Return serialized labels data
    
    # Handle PUT request to update an existing label
    def put(self, request, pk):
        user = request.user # Get the authenticated user
        try:
            # Retrieve the label with the specified primary key and owned by the authenticated user
            label = Label.objects.get(pk=pk, owner=user)
        except Label.DoesNotExist:
            # Return error if label not found
            return Response({'error': 'Label not found'}, status=status.HTTP_404_NOT_FOUND) 
        serializer = LabelSerializer(label, data=request.data) # Deserialize request data into the existing label object
        if serializer.is_valid():
            serializer.save() # Save the updated label
            return Response(serializer.data) # Return serialized label data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # Return errors if serializer is not valid
    
    # Handle DELETE request to delete an existing label
    def delete(self, request, pk):
        user = request.user # Get the authenticated user
        try:
            # Retrieve the label with the specified primary key and owned by the authenticated user
            label = Label.objects.get(pk=pk, owner=user)
        except Label.DoesNotExist:
            # Return error if label not found
            return Response({'error': 'Label not found'}, status=status.HTTP_404_NOT_FOUND)
        label.delete() # Delete the label
        return Response({'message': 'Label deleted successfully'}, status=status.HTTP_200_OK) # Return success message with 200 status code


# Custom filter mixin for retrieving only user-related objects
class UserOwnedMixin: # A mixin class to filter queryset based on the authenticated user.
    def get_queryset(self):
        user = self.request.user # Get the authenticated user from the request
        return super().get_queryset().filter(owner=user)

# View for tasks
class TaskListView(UserOwnedMixin, generics.ListCreateAPIView):
    # view to handle listing and creating tasks for the authenticated user.
    queryset = Task.objects.all()  # Set the queryset to retrieve all tasks
    serializer_class = TaskSerializer # Set the serializer class to serialize tasks
    permission_classes = [IsAuthenticated] # Set the permission classes for the view

# View for labels
class LabelListView(UserOwnedMixin, generics.ListCreateAPIView):
    # view to handle listing and creating labels for the authenticated user.
    queryset = Label.objects.all() # Set the queryset to retrieve all labels
    serializer_class = LabelSerializer # Set the serializer class to serialize labels
    permission_classes = [IsAuthenticated] # Set the permission classes for the view