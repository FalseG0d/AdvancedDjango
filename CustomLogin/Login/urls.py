from . import views
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('login/', views.login_view, name="login"),
    path('register/', views.register_view, name="register"),
    path('logout/', views.logout_view,  name="logout")
]