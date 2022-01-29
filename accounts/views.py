from django.shortcuts import render , redirect
from django.contrib.auth import login, authenticate
from .forms import UserProfileForm, UserForm
from django.views.generic import DetailView, DeleteView, UpdateView
from django.contrib.auth.models import User
from accounts.models import UserProfile
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'accounts/user_detail.html'

# class UserDeleteView(LoginRequiredMixin, DeleteView):
#     model=User
#     success_url=reverse_lazy('index')


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    fields = ['profile_pic']
    template_name = 'accounts/haha.html'
    success_url = reverse_lazy('register:user_dashboard')
    # need to change it to detail
    extra_context = {'userprofile': UserProfileForm()}

    def get_success_url(self):
        return reverse('accounts:user_detail', kwargs={'pk': self.User.pk})


class UserProfileUpateView(LoginRequiredMixin, UpdateView):
    model=UserProfile
    fields=['profile_pic']
