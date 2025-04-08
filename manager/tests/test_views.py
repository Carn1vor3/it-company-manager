from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from manager.models import Position, TaskType, Worker, Task

POSITION_URL = reverse("manager:position-list")
TASK_TYPE_URL = reverse("manager:task-type-list")
WORKER_URL = reverse("manager:worker-list")
TASK_URL = reverse("manager:task-list")

class PublicPositionTest(TestCase):

    def test_login_required(self):
        res = self.client.get(POSITION_URL)
        self.assertNotEqual(res.status_code, 200)

class PrivatePositionTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test_user",
            password="<PASSWORD>",
        )
        self.client.force_login(self.user)

    def test_retrieve_position(self):
        Position.objects.create(name="QA")
        Position.objects.create(name="Developer")
        res = self.client.get(POSITION_URL)
        self.assertEqual(res.status_code, 200)
        positions = Position.objects.all()
        self.assertEqual(list(res.context["position_list"]), list(positions))
        self.assertTemplateUsed(res, "manager/position_list.html")


class PublicTaskTypeTest(TestCase):
    def test_login_required(self):
        res = self.client.get(TASK_TYPE_URL)
        self.assertNotEqual(res.status_code, 200)

class PrivateTaskTypeTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test_user",
            password="<PASSWORD>",
        )
        self.client.force_login(self.user)

    def test_retrieve_task_type(self):
        TaskType.objects.create(name="fix")
        res = self.client.get(TASK_TYPE_URL)
        self.assertEqual(res.status_code, 200)
        task_types = TaskType.objects.all()
        self.assertEqual(list(res.context["task_type_list"]), list(task_types))
        self.assertTemplateUsed(res, "manager/task_type_list.html")


class PublicWorkerTest(TestCase):
    def test_login_required(self):
        res = self.client.get(WORKER_URL)
        self.assertNotEqual(res.status_code, 200)

class PrivateWorkerTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test_user",
            password="<PASSWORD>",
        )
        self.client.force_login(self.user)

    def test_retrieve_worker(self):
        position = Position.objects.create(name="QA")
        worker = get_user_model().objects.create_user(
            username="test_users",
            password="<PASSWORD>",
            position=position,
        )
        res = self.client.get(WORKER_URL)
        self.assertEqual(res.status_code, 200)
        worker = Worker.objects.all()
        self.assertEqual(list(res.context["worker_list"]), list(worker))
        self.assertTemplateUsed(res, "manager/worker_list.html")


class PublicTaskTest(TestCase):
    def test_login_required(self):
        res = self.client.get(TASK_URL)
        self.assertEqual(res.status_code, 200)


class PrivateTaskTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test_user",
            password="<PASSWORD>",
        )
        self.client.force_login(self.user)

    def test_retrieve_task(self):
        worker = Worker.objects.create_user(username="TEST", password="<PASSWORD>")
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
        res = self.client.get(TASK_URL)
        self.assertEqual(res.status_code, 200)
        tasks = Task.objects.all()
        self.assertEqual(list(res.context["task_list"]), list(tasks))
        self.assertTemplateUsed(res, "manager/task_list.html")