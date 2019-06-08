"""Define padrões de URL para learning_logs"""

from django.urls import path 
from . import views

app_name = 'learning_logs'

urlpatterns = [
    path(r'', views.index, name='index'), #Pag inicial
    path(r'topics/', views.topics, name='topics'),
    path(r'topics/<topic_ip>/', views.topic, name='topic'),
    path(r'new_topic/', views.new_topic, name='new_topic'),
    path(r'new_entry/<topic_id>/', views.new_entry, name='new_entry'),
    path(r'edit_entry/<entry_id>/', views.edit_entry, name='edit_entry'),


]