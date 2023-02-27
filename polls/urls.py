from django.urls import path
from . import views # El punto significa que import views desde la misma carpeta polls

urlpatterns = [
    path("", views.index, name="index")
]