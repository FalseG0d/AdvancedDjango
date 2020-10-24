from django.urls import path
from .import views


urlpatterns = [
    path('', views.change_password, name="password"),
]
