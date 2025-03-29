from django import forms
from django.contrib.auth.forms import UserCreationForm

from manager.models import Worker


class WorkerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + ("email", "position", "first_name", "last_name")
