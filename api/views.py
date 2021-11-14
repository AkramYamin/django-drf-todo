from .models import Category, Task
from .serializers import CategorySerializer, TaskSerializer
from rest_framework import generics
from .permissions import IsOwner


class CategoryList(generics.ListCreateAPIView):
    """
        List all the categories from DB
        also allows POST request to create some
    """
    serializer_class = CategorySerializer
    permission_classes = (IsOwner,)

    def get_queryset(self, *args, **kwargs):
        return Category.objects.all().filter(owner=self.request.user)

    def perform_create(self, serializer):
        """
            Override the perform_create from the generic
            serializers.
            :param self: Class
            :param serializer: serializer used to perform actions
        """
        serializer.save(owner=self.request.user)


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    """
        Detail the specific category
        database
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsOwner,)


class TaskList(generics.ListCreateAPIView):
    """
        List all the tasks from DB
        also allows POST request to create some
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsOwner,)

    def get_queryset(self, *args, **kwargs):
        return Task.objects.all().filter(owner=self.request.user)

    def perform_create(self, serializer):
        """
            Override the perform_create from the generic
            serializers.
            :param self: Class
            :param serializer: serializer used to perform actions
        """
        serializer.save(owner=self.request.user)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    """
        Detail the specific task
        database
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsOwner,)
