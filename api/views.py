from .models import Category, Task
from .serializers import CategorySerializer, TaskSerializer
from rest_framework import generics
from .permissions import IsAuthenticatedAndOwner
from datetime import date
from django.db import IntegrityError
from rest_framework import status
from rest_framework.response import Response


class CategoryList(generics.ListCreateAPIView):
    """
        List all the categories from DB
        also allows POST request to create some
    """
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticatedAndOwner,)

    def get_queryset(self, *args, **kwargs):
        return Category.objects.all().filter(owner=self.request.user)

    def create(self, request, *args, **kwargs):
        """
            override create method to handle category duplication exception
        :param request:
        :param args:
        :param kwargs:
        :return: HTTP_409_CONFLICT if the category already exists, otherwise HTTP_201_CREATED code
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            self.perform_create(serializer)
        except IntegrityError:
            return Response(status=status.HTTP_409_CONFLICT)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

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
    permission_classes = (IsAuthenticatedAndOwner,)


class TaskList(generics.ListCreateAPIView):
    """
        List all the tasks from DB
        also allows POST request to create some
    """
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticatedAndOwner,)

    def get_queryset(self, *args, **kwargs):
        """
            Override get_queryset to filter out the finished tasks, and ad return only the tasks
            that the user have access to them, I'm also updating the is_done field whenever the user
            ask for his/her tasks, by checking if the due date less than today, In this way i won't need scheduled
            process to check the due date periodically
            :param args: queryset named parameters
            :param kwargs: queryset keyed parameters
            :return: queryset
        """
        tasks = Task.objects.all().filter(owner=self.request.user, is_done=False)
        for index, task in enumerate(tasks):
            if task.due_date <= date.today():
                task.is_done = True
                task.save()
        return tasks.filter(is_done=False)

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
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticatedAndOwner,)
