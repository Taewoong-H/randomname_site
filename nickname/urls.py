from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('result/<int:pk>/', views.result_name, name='result_name'),
    path('', views.select_catagory, name='select_catagory'),
    path('', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('robots.txt/', TemplateView.as_view(template_name="nickname/robots.txt", content_type="text/plain"), name="project_robots_file"),
]

