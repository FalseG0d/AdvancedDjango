from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.change_password, name='change_password'),
]