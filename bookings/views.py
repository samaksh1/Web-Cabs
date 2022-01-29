from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView , ListView, UpdateView , DeleteView, DetailView
from .forms import BookingForm, FilterForm, MemberForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime
from django.views import generic
from .models import Bookings, Member
from braces.views import LoginRequiredMixin
from django.urls import reverse, reverse_lazy

class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'register/dashboard.html'

    def get_queryset(self):
        return Bookings.objects.all()


#class DetailView(LoginRequiredMixin, generic.DetailView):
 #   model = Bookings
  #  template_name = 'bookings/detail.html'


@login_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            if booking.date < datetime.date.today():
                messages.success(request, "You can't create a booking with a date which has already passed.")
                # return redirect('bookings:bookings_create')
                return render(request, 'bookings/booking_form.html', {'form': form})
            booking.user = request.user
            booking.creator = request.user.username
            booking.save()
            # messages.success(request,  "Booking created successfully ")
            return redirect('register:user_dashboard')
    else:
        form = BookingForm()
        return render(request, 'bookings/booking_form.html', {'form': form})


def filter(request):
    if request.method == 'POST':
        form = FilterForm(request.POST)
        if form.is_valid():
            custom = Bookings.objects.filter(date__gte=datetime.date.today())
            hehehe = []
            if not (form.cleaned_data['start_position'] == ''):
                custom = custom.filter(start_position__contains=form.cleaned_data['start_position'])
                hehehe.append("From:"+form.cleaned_data['start_position'])
            if not (form.cleaned_data['destination'] == ''):
                custom = custom.filter(destination__contains=form.cleaned_data['destination'])
                hehehe.append("To:"+form.cleaned_data['destination'])
            if form.cleaned_data['date']:
                custom = custom.filter(date__iexact=form.cleaned_data['date'])
                hehehe.append("Date:"+form.cleaned_data['date'].strftime('%d-%m-%y'))
            if form.cleaned_data['time']:
                time1 = datetime.datetime.strptime(str(form.cleaned_data['time']), '%H:%M:%S')-datetime.timedelta(hours = 1)
                time2 = datetime.datetime.strptime(str(form.cleaned_data['time']), '%H:%M:%S')+datetime.timedelta(hours = 1)
                custom = custom.filter(time__gte=time1)
                custom = custom.filter(time__lte=time2)
                hehehe.append("Time:"+form.cleaned_data['time'].strftime('%H:%M'))
           # custom = custom.filter(gender__iexact=form.cleaned_data['gender'])
            #hehehe.append("Gender:"+str(form.cleaned_data['gender']))
            context = {}
            context['custom'] = custom
            context['hehehe'] = hehehe
            new_form = FilterForm()
            context['form'] = new_form
            return render(request, 'register/dashboard.html', context)
    else:
        new_form = FilterForm()
        context={}
        context['form'] = new_form
        context['custom'] = Bookings.objects.filter(date__gte=datetime.date.today())
    logger.error("hello")
    return render(request, 'register/dashboard.html', context)


@login_required
def leave_group(request, pk):
    booking = get_object_or_404(Bookings, pk=pk)
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            try:
                member = booking.members.get(name=request.user.username)
                member.delete()
                messages.success(request,  "")
                return redirect('register:user_dashboard')
            except Member.DoesNotExist:
                messages.success(request,  "")
                return redirect('register:user_dashboard')
    else:
        form=MemberForm(request.POST)
    return render(request, 'bookings/leaving_form.html', {'form':form})



def  grp_info(request,pk):
    context={}
    context['custom']=Bookings.objects.get(pk=pk)
    return render(request,'bookings/info.html',context)


@login_required
def my_bookings(request):
    context={}
    hehehe=[]
    context['mybooking']=Bookings.objects.all().filter(creator__iexact=request.user.username).reverse()
    for booking in Bookings.objects.all():
        for member in booking.members.all():
            if request.user.username == member.name:
                hehehe.append(booking)
    context['memberbooking']=hehehe
    return render(request, 'bookings/mybookings.html', context)


class BookingDeleteView(LoginRequiredMixin, DeleteView):
    model = Bookings
    success_url=reverse_lazy('register:user_dashboard')
    success_message=''
    def delete(self, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(*args,**kwargs)


class BookingUpdateView(LoginRequiredMixin, UpdateView):
    model = Bookings
    form_class = BookingForm
    success_url = reverse_lazy('register:user_dashboard')


@login_required
def join_group(request, pk):
    booking=get_object_or_404(Bookings, pk=pk)
    if request.method=='POST':
        form=MemberForm(request.POST)
        if form.is_valid():
            persons=booking.members.all()
            for person in persons:
                if(request.user.username == person.name):
                    messages.success(request,  "")
                    return redirect('register:user_dashboard')

            if (request.user.username==booking.creator):
                messages.success(request,  "")
                return redirect('register:user_dashboard')


            member=form.save(commit=False)
            member.booking=booking
            member.user=request.user
            member.name=request.user.username
            member.save()
            messages.success(request,  "")
            return render(request, 'register/dashboard.html', {'pk': pk})


    else:
        context={}
        context['form']=MemberForm()
        context['custom']=Bookings.objects.get(pk=pk)
    return render(request, 'bookings/joining_form.html ', context)

