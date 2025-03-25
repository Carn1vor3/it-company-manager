from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from manager.models import Worker


def index(request: HttpRequest) -> HttpResponse:
    workers = Worker.objects.all()
    context = {
        "workers": workers,
    }
    return render(request, "manager/index.html", context=context)
