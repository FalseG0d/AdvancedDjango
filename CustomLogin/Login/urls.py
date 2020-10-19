from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path
from .forms import CustomAuthenticationForm

urlpatterns = [
    path('', views.home),
    url(r'^login/$', auth_views.login, {'template_name': 'core/login.html','authentication_form': CustomAuthenticationForm}, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
]