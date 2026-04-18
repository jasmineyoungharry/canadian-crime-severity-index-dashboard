from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('data/', views.data_table, name='data_table'),
    path('charts/', views.charts, name='charts'),
]