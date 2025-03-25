from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from manager.models import Worker, Position
from django.views.generic import ListView


def index(request: HttpRequest) -> HttpResponse:
    workers = Worker.objects.all()
    context = {
        "workers": workers,
    }
    return render(request, "manager/index.html", context=context)

class PositionListView(ListView):
    model = Position
    template_name = "manager/position_list.html"
    context_object_name = "position_list"