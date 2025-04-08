from django.test import TestCase

from manager.forms import WorkerCreationForm
from manager.models import Position


class TestForms(TestCase):
    def test_worker_form_with_first_last_name_and_position(self):
        position = Position.objects.create(name="QA")
        form_data = {
            "username": "test",
            "first_name": "test",
            "last_name": "test",
            "email": "test@example.com",
            "position": position.id,
            "password1": "StrongP@ss123",
            "password2": "StrongP@ss123",
        }
        form = WorkerCreationForm(data=form_data)

        if not form.is_valid():
            print(form.errors)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["username"], form_data["username"])
        self.assertEqual(form.cleaned_data["email"], form_data["email"])
        self.assertEqual(form.cleaned_data["position"], position)
