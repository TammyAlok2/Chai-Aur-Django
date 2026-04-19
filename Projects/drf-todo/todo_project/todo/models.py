from django.db import models
from django.utils import timezone

# Create your models here.


class Todo(models.Model):
    """
    Todo model : each field becomes a database column
    
    """
    title = models.CharField(max_length=200)
    description = models.CharField(blank=True,null=True)
    completed = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    
