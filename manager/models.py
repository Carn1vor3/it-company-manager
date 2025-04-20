
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse



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
        Position, on_delete=models.CASCADE, related_name="worker", null=True, blank=True
    )

    def get_absolute_url(self):
        return reverse("manager:worker-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.username}, {self.email}"


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
    assignees = models.ManyToManyField(Worker, related_name="task")
    priority = models.CharField(choices=PRIORITY_CHOICES, max_length=10, default="Low")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        assignees_names = ", ".join(worker.username for worker in self.assignees.all())
        return (f"Task: ({self.name}),"
                f" Description: ({self.description}),"
                f" Deadline: ({self.deadline}),"
                f" Completed: ({self.is_completed}),"
                f" Task type: ({self.task_type.name}),"
                f" Assignees: ({assignees_names}),"
                f" Priority: ({self.priority})")
