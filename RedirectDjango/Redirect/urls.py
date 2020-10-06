from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('objects',views.objects,name="objects"),
    path('records/<str:pk>/',views.record,name="record"),
]