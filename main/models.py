from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Task(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    deadline = models.DateField(null=True, blank=True)
    description = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f'{self.owner} - {self.name}'
