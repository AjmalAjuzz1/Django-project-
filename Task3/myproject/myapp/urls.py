from django import views
from django.urls import path,include
# from .import views

from . import views

urlpatterns = [
    path('', views.index),
    path('myapp/',views.ques),
     path('<int:id>/',views.option)
    
]