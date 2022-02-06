from django.shortcuts import render
from .models import Todo
from .serializers import TodoSerializer
from rest_framework import generics
# Create your views here.


class TodoList(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer