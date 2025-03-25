from django.urls import path
from manager.views import index

urlpatterns = [
    path("home/", index, name="home"),
]

app_name = "manager"
