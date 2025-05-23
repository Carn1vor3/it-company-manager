from django.urls import path

from manager.views import (
    index,
    PositionListView,
    PositionDetailView,
    PositionCreateView,
    PositionUpdateView,
    PositionDeleteView,

    TaskTypeListView,
    TaskTypeCreateView,
    TaskTypeUpdateView,
    TaskTypeDetailView,
    TaskTypeDeleteView,

    WorkerListView,
    WorkerDetailView,
    WorkerCreateView,
    WorkerDeleteView,
    WorkerPositionUpdateView,

    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    task_assign_unassign, logout_view, UserLoginView, logged_out_view,

)

urlpatterns = [
    path("", index, name="home"),
    path("position/", PositionListView.as_view(), name="position-list"),
    path("position/<int:pk>/detail/", PositionDetailView.as_view(), name="position-detail"),
    path("position/create/", PositionCreateView.as_view(), name="position-create"),
    path("position/<int:pk>/update/", PositionUpdateView.as_view(), name="position-update"),
    path("position/<int:pk>/delete/", PositionDeleteView.as_view(), name="position-delete"),

    path("tasktype/", TaskTypeListView.as_view(), name="task-type-list"),
    path("tasktype/<int:pk>/detail/", TaskTypeDetailView.as_view(), name="task-type-detail"),
    path("tasktype/create/", TaskTypeCreateView.as_view(), name="task-type-create"),
    path("tasktype/<int:pk>/update/", TaskTypeUpdateView.as_view(), name="task-type-update"),
    path("tasktype/<int:pk>/delete/", TaskTypeDeleteView.as_view(), name="task-type-delete"),

    path("worker/", WorkerListView.as_view(), name="worker-list"),
    path("worker/<int:pk>/detail/", WorkerDetailView.as_view(), name="worker-detail"),
    path("worker/create/", WorkerCreateView.as_view(), name="worker-create"),
    path("worker/<int:pk>/delete/", WorkerDeleteView.as_view(), name="worker-delete"),
    path("worker/<int:pk>/update/", WorkerPositionUpdateView.as_view(), name="worker-position-update"),

    path("task/", TaskListView.as_view(), name="task-list"),
    path("task/<int:pk>/detail/", TaskDetailView.as_view(), name="task-detail"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("task/<int:pk>/assign_unassign/", task_assign_unassign, name="task-assign-unassign"),
    path('logged_out/', logged_out_view, name='logged_out'),
]


app_name = "manager"
