from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'register'


urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.filter, name='user_dashboard'),
    path('logout/', auth_views.LogoutView.as_view(template_name='register/homepage.html'), name='user_logout'),
]