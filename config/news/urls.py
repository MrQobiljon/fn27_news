from django.urls import path

from .views import home, about, contact, timer

urlpatterns = [
    path('', home),
    path('about/', about),
    path('contact/', contact),
    path('view-timer/', timer),
]