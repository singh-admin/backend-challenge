"""
URL configuration for Assignment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks.views import TaskView, LabelView, obtain_auth_token_view, TaskListView, LabelListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', obtain_auth_token_view, name='api-token'),
    path('tasks/', TaskView.as_view()),  # GET all tasks for authenticated user
    path('tasks/my-tasks/', TaskListView.as_view(), name='my-task-list'),  # GET all tasks for authenticated user only
    path('tasks/<int:pk>/', TaskView.as_view()),  # GET, PUT, DELETE for specific task (pk)
    path('labels/', LabelView.as_view()),  # GET all labels for authenticated user
    path('labels/<int:pk>/', LabelView.as_view()),  # GET, PUT, DELETE for specific label (pk)
    path('labels/my-labels/', LabelListView.as_view(), name='my-label-list'),  # GET all labels for authenticated user only
]

