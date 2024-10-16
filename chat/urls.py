from django.contrib.auth import views as auth_views   # alias to avoid namespace conflict
from django.urls import path

from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.CustomLoginView.as_view(template_name='chat/login.html'), name='login'),
    path('logout/', views.user_logout, name='logout'),
]
