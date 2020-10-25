from django.urls import path
from . import views

urlpatterns = [
    path(r'index/', views.index, name='index'),
    path(r'table/', views.table, name='table'),
]