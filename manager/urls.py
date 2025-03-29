from django.urls import path
from manager.views import (
    index,
    PositionListView,
    PositionDetailView,
    TaskTypeListView,
    WorkerListView,
    TaskListView,
    WorkerDetailView,
    TaskDetailView,
)

urlpatterns = [
    path("", index, name="home"),
    path("position/", PositionListView.as_view(), name="position-list"),
    path("position/<int:pk>/detail/", PositionDetailView.as_view(), name="position-detail"),

    path("tasktype/", TaskTypeListView.as_view(), name="task-type-list"),
    path("worker/", WorkerListView.as_view(), name="worker-list"),
    path("worker/<int:pk>/detail/", WorkerDetailView.as_view(), name="worker-detail"),
    path("task/", TaskListView.as_view(), name="task-list"),
    path("task/<int:pk>/detail/", TaskDetailView.as_view(), name="task-detail"),

]


app_name = "manager"
