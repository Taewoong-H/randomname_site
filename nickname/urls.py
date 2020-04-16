from django.urls import path
from . import views

urlpatterns = [
    path('result/<int:pk>/', views.result_name, name='result_name'),
    path('', views.select_catagory, name='select_catagory'),
    path('', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
]

'''
path('catch/<str:message>', views.place_name, name='place_name'),
'''
