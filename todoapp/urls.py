from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.TodoList.as_view()),
    path('todos/<int:pk>/', views.TodoDetail.as_view()),
    # Part 2 add users methods 
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('signup', views.SignUpUserView.as_view()),
    path('groups/', views.TodoGroupList.as_view()),
    path('groups/<int:pk>/', views.TodoGroupDetail.as_view()),
    
]
