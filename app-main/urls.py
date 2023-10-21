from django.urls import path
from . import views

app_name = 'app'


urlpatterns = [
    path('', views.index),
    path('add/', views.add),
]
