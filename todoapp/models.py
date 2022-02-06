from django.db import models

class TodoGroup(models.Model):
    owner = models.ForeignKey('auth.User', related_name='todo_groups', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

# Create your models here.
class Todo(models.Model):
    owner = models.ForeignKey('auth.User', related_name='todos', on_delete=models.CASCADE)
    todo_group = models.ForeignKey(TodoGroup, on_delete=models.CASCADE, default=None, blank=True, null=True)
    title = models.CharField(max_length=100)
    memo = models.TextField(blank = True)
    due_date = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default = False)
    assigned_to = models.CharField(max_length=100)

    class Meta:
        ordering = ['-is_completed','due_date']

    def __str__(self):
        return self.title
