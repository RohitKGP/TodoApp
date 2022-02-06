from django.shortcuts import render
from .models import Todo, TodoGroup
from .serializers import TodoSerializer, TodoGroupSerializer, UserSerializer, SignUpSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import mixins, viewsets
from django.contrib.auth import get_user_model
# Create your views here.


class TodoList(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TodoGroupList(generics.ListCreateAPIView):
    queryset = TodoGroup.objects.all()
    serializer_class = TodoGroupSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TodoGroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoGroup.objects.all()
    serializer_class = TodoGroupSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SignUpUserView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = get_user_model().objects.all() 
    serializer_class = SignUpSerializer
