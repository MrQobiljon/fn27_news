from django.shortcuts import render

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, HttpRequest


def home(request: WSGIRequest):
    return render(request, 'index.html')


def about(request: WSGIRequest):
    return HttpResponse("Biz haqimizda!")


def contact(request: WSGIRequest):
    return HttpResponse('Contact')


def timer(request):
    return render(request, 'timer.html')