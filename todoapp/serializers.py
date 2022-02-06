from .models import Todo, TodoGroup
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

class TodoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    todo_group = serializers.ReadOnlyField(source='todo_group.title')
    class Meta:
        model = Todo
        fields = ['id', 'owner', 'todo_group', 'title', 'memo', 'due_date', 'is_completed', 'assigned_to']

class UserSerializer(serializers.ModelSerializer):
    todos = serializers.PrimaryKeyRelatedField(many=True, queryset=Todo.objects.all())
    groups = serializers.PrimaryKeyRelatedField(many=True, queryset=TodoGroup.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'todos', 'groups']

class TodoGroupSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    todo_set = serializers.PrimaryKeyRelatedField(many=True, queryset=Todo.objects.all())
    class Meta:
        model = TodoGroup
        fields = ['id', 'title', 'owner', 'todo_set']





class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email', 'password', ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = get_user_model()(**validated_data)

        user.set_password(validated_data['password'])
        user.save()

        return user
