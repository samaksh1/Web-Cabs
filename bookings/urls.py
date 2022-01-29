from django.urls import path, re_path
from . import views

app_name = 'bookings'

urlpatterns = [
    path('create/', views.create_booking, name='bookings_create'),
    path('', views.IndexView.as_view(), name='index'),
    path('mybookings/', views.my_bookings, name='my_bookings'),
    #path('<pk>/', views.DetailView.as_view(), name='detail'),
    re_path(r'^(?P<pk>\d+)/update/$', views.BookingUpdateView.as_view(template_name='bookings/bookings_update.html'), name='bookings_update'),
    re_path(r'^(?P<pk>\d+)/delete/$', views.BookingDeleteView.as_view(template_name='bookings/bookings_delete.html'), name='bookings_delete'),
    re_path(r'^(?P<pk>\d+)/join/$', views.join_group , name='group_join'),
    re_path(r'^(?P<pk>\d+)/leave/$', views.leave_group , name='group_leave'),
    re_path(r'^(?P<pk>\d+)/info/$', views.grp_info, name='group_info'),

]
