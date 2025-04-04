from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import CheckboxSelectMultiple
from django.forms.fields import MultipleChoiceField

from manager.models import Worker, Position, Task


def capacity_validator(value):
    if value.name in ["Admin", "Superuser"]:
        raise forms.ValidationError("You cannot choose this position.")
    if value.worker.count() >= 10:
        raise forms.ValidationError(f"The position '{value.name}' is full.")


class WorkerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name", "email", "position")

    def clean_position(self):
        position = self.cleaned_data.get("position")
        if position:
            capacity_validator(position)
        return position


class WorkerPositionUpdateForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ("position",)

    def clean_position(self):
        position = self.cleaned_data.get("position")
        if position:
            capacity_validator(position)
        return position

class TaskForm(forms.ModelForm):
    assignees = forms.ModelChoiceField(
        queryset=get_user_model().objects.all(),
        widget=CheckboxSelectMultiple(),
    )
    class Meta:
        model = Task
        fields = "__all__"


class PositionSearchForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name"}),
    )


class TaskTypeSearchForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name"}),
    )


class TaskSearchForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name"}),
    )