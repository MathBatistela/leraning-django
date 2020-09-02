from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("matheus", views.matheus, name="matheus"),
    path("<str:name>", views.greet, name="greet")
]