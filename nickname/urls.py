from django.urls import path
from . import views

urlpatterns = [
    path('', views.select_name, name='select_name'),
]