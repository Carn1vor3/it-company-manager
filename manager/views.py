from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from manager.forms import WorkerCreationForm
from manager.models import Worker, Position, TaskType, Task
from django.views.generic import ListView, DetailView, CreateView, UpdateView


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

class PositionListView(LoginRequiredMixin, ListView):
    model = Position
    template_name = "manager/position_list.html"
    context_object_name = "position_list"
    paginate_by = 5


class PositionDetailView(LoginRequiredMixin, DetailView):
    model = Position
    template_name = "manager/position_detail.html"
    context_object_name = "position_detail"


class PositionCreateView(LoginRequiredMixin, CreateView):
    model = Position
    template_name = "manager/position_create.html"
    context_object_name = "position_create"
    fields = "__all__"
    success_url = "/manager/position/"


class PositionUpdateView(LoginRequiredMixin, UpdateView):
    model = Position
    template_name = "manager/position_update.html"
    context_object_name = "position"
    fields = "__all__"
    success_url = "/manager/position/"


class TaskTypeListView(LoginRequiredMixin, ListView):
    model = TaskType
    template_name = "manager/task_type_list.html"
    context_object_name = "task_type_list"
    paginate_by = 5


class TaskTypeCreateView(LoginRequiredMixin, CreateView):
    model = TaskType
    template_name = "manager/task_type_create.html"
    context_object_name = "task_type_create"
    fields = "__all__"
    success_url = "/manager/tasktype/"


class TaskTypeDetailView(LoginRequiredMixin, DetailView):
    model = TaskType
    template_name = "manager/task_type_detail.html"
    context_object_name = "task_type_detail"


class TaskTypeUpdateView(LoginRequiredMixin, UpdateView):
    model = TaskType
    template_name = "manager/task_type_update.html"
    context_object_name = "task_type"
    fields = "__all__"
    success_url = "/manager/tasktype/"

class WorkerListView(LoginRequiredMixin, ListView):
    model = Worker
    template_name = "manager/worker_list.html"
    context_object_name = "worker_list"
    paginate_by = 5


class WorkerDetailView(LoginRequiredMixin, DetailView):
    model = Worker
    template_name = "manager/worker_detail.html"
    context_object_name = "worker_detail"


class WorkerCreateView(LoginRequiredMixin, CreateView):
    model = Worker
    template_name = "manager/worker_create.html"
    context_object_name = "worker_create"
    form_class = WorkerCreationForm
    success_url = "/manager/worker/"


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "manager/task_list.html"
    context_object_name = "task_list"
    paginate_by = 5


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "manager/task_detail.html"
    context_object_name = "task_detail"


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "manager/task_create.html"
    context_object_name = "task_create"
    fields = "__all__"
    success_url = "/manager/task/"
