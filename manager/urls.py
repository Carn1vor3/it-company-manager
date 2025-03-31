from django.urls import path
from manager.views import (
    index,
    PositionListView,
    PositionDetailView,
    PositionCreateView,
    PositionUpdateView,
    TaskTypeListView,
    TaskTypeCreateView,
    TaskTypeUpdateView,
    TaskTypeDetailView,
    WorkerListView,
    WorkerDetailView,
    WorkerCreateView,
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
)

urlpatterns = [
    path("", index, name="home"),
    path("position/", PositionListView.as_view(), name="position-list"),
    path("position/<int:pk>/detail/", PositionDetailView.as_view(), name="position-detail"),
    path("position/create/", PositionCreateView.as_view(), name="position-create"),
    path("position/<int:pk>/update/", PositionUpdateView.as_view(), name="position-update"),

    path("tasktype/", TaskTypeListView.as_view(), name="task-type-list"),
    path("tasktype/<int:pk>/detail/", TaskTypeDetailView.as_view(), name="task-type-detail"),
    path("tasktype/create/", TaskTypeCreateView.as_view(), name="task-type-create"),
    path("tasktype/<int:pk>/update/", TaskTypeUpdateView.as_view(), name="task-type-update"),

    path("worker/", WorkerListView.as_view(), name="worker-list"),
    path("worker/<int:pk>/detail/", WorkerDetailView.as_view(), name="worker-detail"),
    path("worker/create/", WorkerCreateView.as_view(), name="worker-create"),

    path("task/", TaskListView.as_view(), name="task-list"),
    path("task/<int:pk>/detail/", TaskDetailView.as_view(), name="task-detail"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
]


app_name = "manager"
