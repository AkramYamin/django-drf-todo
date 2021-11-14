from .models import Category, Task
from .serializers import CategorySerializer, TaskSerializer
from rest_framework import generics


class CategoryList(generics.ListCreateAPIView):
    """
        List all the categories from DB
        also allows POST request to create some
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    """
        Detail the specific category
        database
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TaskList(generics.ListCreateAPIView):
    """
        List all the tasks from DB
        also allows POST request to create some
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    """
        Detail the specific task
        database
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
