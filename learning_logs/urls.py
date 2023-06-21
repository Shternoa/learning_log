"""Определяет схемы URL для learning_logs."""

from django.urls import path

from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'), path('topics/', views.topics, name='topics'),
    path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    path(r'^new_topic/$', views.new_topic, name='new_topic'),
    path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry')
]
