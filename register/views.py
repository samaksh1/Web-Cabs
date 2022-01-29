from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.views import generic
from .forms import SignUpForm
from bookings.forms import FilterForm
from bookings.models import Bookings
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.views.generic import CreateView , ListView, UpdateView , DeleteView, DetailView
from braces.views import LoginRequiredMixin


def index(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
            return redirect('register:user_dashboard')
    else:
        form = SignUpForm()
    return render(request, 'register/index.html', {'form': form})


def homepage(request):
    if request.method == 'POST':
        #form = SignUpForm(request.POST)
        #if form.is_valid():
         #   form.save()
            #username = form.cleaned_data.get('username')
            #raw_password = form.cleaned_data.get('password1')
            user = authenticate(request.POST)
            if user is not None:
                login(request, user)
                return redirect('register:user_dashboard')
   #     form = SignUpForm()
    return render(request, 'register/homepage.html', {})


#@login_required()
#def user_dashboard(request):
#    return render(request, 'register/dashboard.html',)

#class UserDetailView(LoginRequiredMixin, ListView):
    #model = User
    #template_name='register/dashboard.html'


def filter(request):
    if request.method=='POST':
        form=FilterForm(request.POST)
        if form.is_valid():

            custom=Bookings.objects.filter(date__gte=datetime.date.today())
            hehehe=[]
            if(not (form.cleaned_data['start_position']=='')):
                custom=custom.filter(start_position__contains=form.cleaned_data['start_position'])
                hehehe.append("From:"+form.cleaned_data['start_position'])
            if(not (form.cleaned_data['destination']=='')):
                custom=custom.filter(destination__contains=form.cleaned_data['destination'])
                hehehe.append("To:"+form.cleaned_data['destination'])
            if((form.cleaned_data['date'])):
                custom=custom.filter(date__iexact=form.cleaned_data['date'])

                hehehe.append("Date:"+form.cleaned_data['date'].strftime('%d-%m-%y'))
            if(form.cleaned_data['time']):
                time1=datetime.datetime.strptime(str(form.cleaned_data['time']), '%H:%M:%S')-datetime.timedelta(hours=1)
                time2=datetime.datetime.strptime(str(form.cleaned_data['time']), '%H:%M:%S')+datetime.timedelta(hours=1)
                custom=custom.filter(time__gte=time1)
                custom=custom.filter(time__lte=time2)
                hehehe.append("Time:"+form.cleaned_data['time'].strftime('%H:%M'))
            #custom=custom.filter(gender__iexact=form.cleaned_data['gender'])
            #hehehe.append("Gender:"+str(form.cleaned_data['gender']))
            context={}
            context['custom']=custom
            context['hehehe']=hehehe
            new_form=FilterForm()
            context['form'] = new_form
            return render(request, 'register/dashboard.html', context)
    else:
        new_form= FilterForm()
        context={}
        context['form']=new_form
        context['custom']=Bookings.objects.filter(date__gte=datetime.date.today())
    return render(request, 'register/dashboard.html', context)