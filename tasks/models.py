from django.db import models
from django.utils import timezone

# Create your models here.
class Tasks(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f"{self.id}: {self.name} is completed: {self.status}"