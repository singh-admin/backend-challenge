# Import necessary modules
from django.test import TestCase
from ..models import Task, Label
from django.contrib.auth.models import User

# Test case for the Task model.
class TaskModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_user') # Create a test user
        # Create a test task associated with the singh user
        self.task = Task.objects.create(title='Test Task', description='Testing Models', completed=False, owner=self.user)
    
    # Test method to verify task creation.
    def test_task_creation(self):
        # Assert that the task attributes match the expected values
        self.assertEqual(self.task.title, 'Test Task')
        self.assertEqual(self.task.description, 'Testing Models')
        self.assertFalse(self.task.completed)
        self.assertEqual(self.task.owner, self.user)

# Test case for the Label model.
class LabelModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_user')  # Create a test user
        # Create a test label associated with the test user
        self.label = Label.objects.create(name='Test Label', owner=self.user)

    # Test method to verify label creation.
    def test_label_creation(self):
        # Assert that the label attributes match the expected values
        self.assertEqual(self.label.name, 'Test Label')
        self.assertEqual(self.label.owner, self.user)
