from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("producto/", views.producto, name="producto"),
    path("contacto/", views.contacto, name="contacto"),
]
