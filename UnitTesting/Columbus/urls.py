from .import views
from django.urls import path

urlpatterns = [
    path('', views.i_was_here),
]
