from django.contrib import admin
from django.urls import path, include
from bankmain import views
urlpatterns = [

    path('', views.home)
]
