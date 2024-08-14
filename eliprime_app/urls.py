from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("engine/", views.diagnostic_form, name="diagnostic_form"),
]
