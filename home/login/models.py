from django.db import models

# Create your models here.
# A task has title, description, task, status (pending/complete)

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    task = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    
