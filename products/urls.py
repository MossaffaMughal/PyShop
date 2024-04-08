from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),  # '' means root of this app
    path('new', views.new)
]
