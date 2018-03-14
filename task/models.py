from django.db import models
from django.utils import timezone

# Create your models here.

class Task(models.Model):
    created = models.DateTimeField(default=timezone.now)
    creator = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    executor = models.Field('auth.User')
    deadline = models.DateField()
    description = models.TextField()