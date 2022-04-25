from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('group/<slug:any_str>/', views.group_posts)
] 