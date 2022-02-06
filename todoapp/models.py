from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank = True)
    due_date = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default = False)
    assigned_to = models.CharField(max_length=100)

    class Meta:
        ordering = ['-is_completed','due_date']

    def __str__(self):
        return self.title