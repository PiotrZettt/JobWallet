from django.urls import path
from . import views

app_name = 'analysis'

urlpatterns = [
    path('index', views.index, name='index' ),
]