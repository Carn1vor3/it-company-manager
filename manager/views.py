from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from manager.models import Worker, Position, TaskType, Task
from django.views.generic import ListView, DetailView


def index(request: HttpRequest) -> HttpResponse:
    workers = Worker.objects.count()
    positions = Position.objects.count()
    tasks = Task.objects.count()
    task_type = TaskType.objects.count()
    context = {
        "workers": workers,
        "positions": positions,
        "tasks": tasks,
        "task_type": task_type,
    }
    return render(request, "manager/index.html", context=context)

class PositionListView(ListView):
    model = Position
    template_name = "manager/position_list.html"
    context_object_name = "position_list"


class PositionDetailView(DetailView):
    model = Position
    template_name = "manager/position_detail.html"
    context_object_name = "position_detail"


class TaskTypeListView(ListView):
    model = TaskType
    template_name = "manager/task_type_list.html"
    context_object_name = "task_type_list"


class WorkerListView(ListView):
    model = Worker
    template_name = "manager/worker_list.html"
    context_object_name = "worker_list"


class WorkerDetailView(DetailView):
    model = Worker
    template_name = "manager/worker_detail.html"
    context_object_name = "worker_detail"


class TaskListView(ListView):
    model = Task
    template_name = "manager/task_list.html"
    context_object_name = "task_list"


class TaskDetailView(DetailView):
    model = Task
    template_name = "manager/task_detail.html"
    context_object_name = "task_detail"


def logged_out(request):
    return render(request, "registration/logged_out.html")