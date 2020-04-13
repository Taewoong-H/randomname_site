from django.urls import path
from . import views

urlpatterns = [
    path('result/<int:pk>/', views.result_name, name='result_name'),
    path('', views.select_catagory, name='select_catagory'),
]
'''
path('result/<int:pk>/', views.result_name, name='result_name'),
'''