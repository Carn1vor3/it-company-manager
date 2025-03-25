from random import choices

from django.contrib.auth.models import AbstractUser
from django.db import models

from it_company_manager.settings import AUTH_USER_MODEL


class Position(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class TaskType(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(
        Position, on_delete=models.CASCADE, related_name="worker"
    )


class Task(models.Model):
    PRIORITY_CHOICES = (
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High"),
        ("Critical", "Critical"),
    )

    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    task_type = models.ForeignKey(
        TaskType, on_delete=models.CASCADE, related_name="task"
    )
    assignees = models.ManyToManyField(Worker, related_name="assignee")
    priority = models.CharField(choices=PRIORITY_CHOICES, max_length=10, default="Low")
