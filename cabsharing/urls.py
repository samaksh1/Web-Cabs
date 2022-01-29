from django.contrib import admin
from django.urls import path, include
#from register.views import homepage
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', include('register.urls')),
    path('', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    #path('accounts/', include('django.contrib.auth.urls')),
    path('', auth_views.LoginView.as_view(template_name='register/homepage.html'), name='user_login'),
    path('bookings/', include('bookings.urls')),
    #path('password_reset', auth_views.PasswordResetView.as_view(template_name='register/password_reset_form.html', name = 'password_reset')),
]







#path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='user_login'),