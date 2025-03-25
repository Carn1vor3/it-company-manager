from django.urls import path
from manager.views import index, PositionListView

urlpatterns = [
    path("home/", index, name="home"),
    path("position/", PositionListView.as_view(), name="position-list"),
]

app_name = "manager"
