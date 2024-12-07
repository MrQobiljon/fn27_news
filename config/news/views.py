from django.shortcuts import render

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, HttpRequest

from .models import Category, Post



def home(request: WSGIRequest):
    posts = Post.objects.all()
    categories = Category.objects.all()
    context = {
        "posts": posts,
        "categories": categories
    }
    return render(request, 'index.html', context=context)


def about(request: WSGIRequest):
    return HttpResponse("Biz haqimizda!")


def contact(request: WSGIRequest):
    return HttpResponse('Contact')


def timer(request):
    return render(request, 'timer.html')