"""Define padrões de URL para users"""

from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

app_name = 'users'

urlpatterns = [
    path(r'login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path(r'logout/', views.logout_view, name='logout'),
    path(r'register/', views.register, name='register'),
]