from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from manager.models import Position


class AdminSiteTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin", password="<PASSWORD>"
        )
        self.client.force_login(self.admin_user)
        position = Position.objects.create(name="position")
        self.worker = get_user_model().objects.create_user(
            username="test_worker",
            password="<PASSWORD>",
            position=position,
        )

    def test_worker_position_listed(self):
        url = reverse("admin:manager_worker_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.worker.position.name)

    def test_worker_detail_position_listed(self):
        url = reverse("admin:manager_worker_change", args=[self.worker.pk])
        res = self.client.get(url)
        self.assertContains(res, self.worker.position.name)

    def test_worker_detail_add_position_listed(self):
        url = reverse("admin:manager_worker_add")
        res = self.client.get(url)
        self.assertContains(res, "position")
