from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse

from manager.forms import WorkerCreationForm, WorkerPositionUpdateForm, TaskForm, PositionSearchForm, \
    TaskTypeSearchForm, TaskSearchForm, WorkerSearchForm, UserLoginForm
from manager.models import Worker, Position, TaskType, Task
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import logout


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
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PositionListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = PositionSearchForm(
            initial={"name": name},
        )
        return context

    def get_queryset(self):
        queryset = Position.objects.all()
        form = PositionSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class PositionDetailView(LoginRequiredMixin, DetailView):
    model = Position
    template_name = "manager/position_detail.html"
    context_object_name = "position_detail"


class PositionCreateView(LoginRequiredMixin, CreateView):
    model = Position
    template_name = "manager/position_create.html"
    context_object_name = "position_create"
    fields = "__all__"
    success_url = "/position/"


class PositionUpdateView(LoginRequiredMixin, UpdateView):
    model = Position
    template_name = "manager/position_update.html"
    context_object_name = "position"
    fields = "__all__"
    success_url = "/position/"


class PositionDeleteView(LoginRequiredMixin, DeleteView):
    model = Position
    template_name = "manager/position_confirmation_delete.html"
    context_object_name = "position"
    success_url = "/position/"


class TaskTypeListView(LoginRequiredMixin, ListView):
    model = TaskType
    template_name = "manager/task_type_list.html"
    context_object_name = "task_type_list"
    paginate_by = 6

    def get_context_data(self, *, object_list = ..., **kwargs):
        context = super(TaskTypeListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = TaskTypeSearchForm(
            initial={"name": name},
        )
        return context

    def get_queryset(self):
        queryset = TaskType.objects.all()
        form = TaskTypeSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class TaskTypeCreateView(LoginRequiredMixin, CreateView):
    model = TaskType
    template_name = "manager/task_type_create.html"
    context_object_name = "task_type_create"
    fields = "__all__"
    success_url = "/tasktype/"


class TaskTypeDetailView(LoginRequiredMixin, DetailView):
    model = TaskType
    template_name = "manager/task_type_detail.html"
    context_object_name = "task_type_detail"


class TaskTypeUpdateView(LoginRequiredMixin, UpdateView):
    model = TaskType
    template_name = "manager/task_type_update.html"
    context_object_name = "task_type"
    fields = "__all__"
    success_url = "/tasktype/"


class TaskTypeDeleteView(LoginRequiredMixin, DeleteView):
    model = TaskType
    template_name = "manager/task_type_confirmation_delete.html"
    context_object_name = "task_type"
    success_url = "/tasktype/"


class WorkerListView(LoginRequiredMixin, ListView):
    model = Worker
    template_name = "manager/worker_list.html"
    context_object_name = "worker_list"
    paginate_by = 6

    def get_context_data(self, *, object_list = ..., **kwargs):
        context = super(WorkerListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["search_form"] = WorkerSearchForm(
            initial={"username": username},
        )
        return context

    def get_queryset(self):
        queryset = Worker.objects.all()
        form = WorkerSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(username__icontains=form.cleaned_data["username"])
        return queryset


class WorkerDetailView(LoginRequiredMixin, DetailView):
    model = Worker
    template_name = "manager/worker_detail.html"
    context_object_name = "worker_detail"


class WorkerCreateView(LoginRequiredMixin, CreateView):
    model = Worker
    template_name = "manager/worker_create.html"
    context_object_name = "worker_create"
    form_class = WorkerCreationForm
    success_url = "/worker/"


class WorkerDeleteView(LoginRequiredMixin, DeleteView):
    model = Worker
    template_name = "manager/worker_confirmation_delete.html"
    context_object_name = "worker"
    success_url = "/worker/"


class WorkerPositionUpdateView(LoginRequiredMixin, UpdateView):
    model = Worker
    template_name = "manager/worker_position_update.html"
    form_class = WorkerPositionUpdateForm
    context_object_name = "worker_position_update"
    success_url = "/worker/"


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "manager/task_list.html"
    context_object_name = "task_list"
    paginate_by = 6

    def get_context_data(self, *, object_list = ..., **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = TaskSearchForm(
            initial={"name": name},
        )
        return context

    def get_queryset(self):
        queryset = Task.objects.all()
        form = TaskSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "manager/task_detail.html"
    context_object_name = "task_detail"


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = "manager/task_create.html"
    context_object_name = "task_create"
    success_url = "/task/"


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "manager/task_confirmation_delete.html"
    context_object_name = "task"
    success_url = "/task/"



class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "manager/task_update.html"
    context_object_name = "task"
    success_url = "/task/"


def task_assign_unassign(request:HttpRequest, pk:int):
    task = get_object_or_404(Task, id=pk)
    if request.user not in task.assignees.all():
        task.assignees.add(request.user)
    else:
        task.assignees.remove(request.user)

    return HttpResponseRedirect(reverse("manager:task-detail", args=[pk]))


class UserLoginView(LoginView):
  template_name = 'accounts/sign-in.html'
  form_class = UserLoginForm

def logout_view(request):
  logout(request)
  return redirect("manager:logged_out")

def logged_out_view(request):
    return render(request, 'accounts/logged_out.html')
