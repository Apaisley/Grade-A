from django.urls import  path
from django.contrib import admin
from . import views
from .views import current_datetime

urlpatterns =[
    
    path('', views.index, name='index'),
    path('datetime', views.current_datetime, name='current_datetime'),
    
]