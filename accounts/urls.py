from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'accounts'

urlpatterns = [
    #path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='user_login'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='accounts/password_change_form.html') , name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'), name='password_change_done'),
    path('password_reset', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset_form.html',email_template_name='accounts/password_reset_email.html',subject_template_name='accounts/password_reset_subject.txt'),name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('password_reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset/done', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
    # normal urls are not working in my case

    re_path(r'^(?P<pk>\d+)/detail/$', views.UserDetailView.as_view(), name='user_detail'),
    # re_path(r'^(?P<pk>\d+)/delete/$', views.UserDeleteView.as_view(template_name='accounts/user_delete.html'), name='user_delete'),

    re_path(r'^(?P<pk>\d+)/update/$', views.UserUpdateView.as_view(template_name='accounts/haha.html'), name='user_update'),


    ]