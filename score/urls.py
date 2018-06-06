"""Url path and include modules for routing views"""
from django.urls import path, include
from . import views

app_name = "score"

urlpatterns = [
    path('', views.ScoresCreate.as_view(), name='index'),
    path('results/', views.results, name='results')
]