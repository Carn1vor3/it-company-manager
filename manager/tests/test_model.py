from datetime import datetime

from django.test import TestCase

from manager.models import Position, TaskType, Worker, Task


class TestModel(TestCase):
    def test_position_str(self):
        position = Position.objects.create(name="TEST")
        self.assertEqual(str(position), position.name)

    def test_task_type_str(self):
        task_type = TaskType.objects.create(name="TEST")
        self.assertEqual(str(task_type), task_type.name)

    def test_worker_str(self):
        worker = Worker.objects.create_user(username="TEST", password="<PASSWORD>", email="<EMAIL>")
        self.assertEqual(str(worker), f"{worker.username}, {worker.email}")

    def test_task_str(self):
        worker = Worker.objects.create_user(username="TEST", password="<PASSWORD>", email="<EMAIL>")
        task_type = TaskType.objects.create(name="TEST")

        task = Task.objects.create(
            name="TEST",
            description="TEST",
            deadline=datetime.now(),
            is_completed=False,
            task_type=task_type,
            priority=1,
        )
        task.assignees.add(worker)

        assignees_names = ", ".join(w.username for w in task.assignees.all())
        expected_str = (
            f"Task: ({task.name}),"
            f" Description: ({task.description}),"
            f" Deadline: ({task.deadline}),"
            f" Completed: ({task.is_completed}),"
            f" Task type: ({task.task_type.name}),"
            f" Assignees: ({assignees_names}),"
            f" Priority: ({task.priority})"
        )
        self.assertEqual(str(task), expected_str)