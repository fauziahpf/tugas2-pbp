from django.db import models
from django.contrib.auth.models import User

# Create models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    title = models.CharField(max_length=30)
    description = models.TextField()