from django.urls import path
from manager.views import (
    index,
    PositionListView,
    TaskTypeListView,
    WorkerListView,
    TaskListView,
)

urlpatterns = [
    path("home/", index, name="home"),
    path("position/", PositionListView.as_view(), name="position-list"),

    path("tasktype/", TaskTypeListView.as_view(), name="task-type-list"),
    path("worker/", WorkerListView.as_view(), name="worker-list"),
    path("task/", TaskListView.as_view(), name="task-list"),
]

app_name = "manager"
