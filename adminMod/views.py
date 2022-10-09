from django.shortcuts import render,redirect,get_object_or_404
from .models import adminMod_appointment, appointment
from datetime import datetime
from django.db import models
from django.utils.dateparse import parse_date, parse_time
from .forms import AppointmentForm
from django.contrib.auth import authenticate, login


# Create your views here.
def get_appointments(request):
    appointments = appointment.objects.all()

    context = {
        'appointments': appointments
    }

    return render(request, 'adminMod/admin_list.html', context)


def add(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = "Sample address"
        email = "sample@gmail.com"
        mobile_ext = request.POST.get('mobile-ext')
        mobile = request.POST.get('mobile')
        problem_description = request.POST.get('symptoms')
        date=models.DateTimeField()
        date = request.POST.get('date')
        converted_date = parse_date(date)
        time = models.TimeField()    
        time = request.POST.get('time')
        converted_time = parse_time(time)
        mydatetime = datetime.combine(converted_date, converted_time)
        adminMod_appointment.objects.create(firstname=first_name, lastname=last_name,
        address=address, email=email, mobile_ext=mobile_ext, mobile=mobile, complaint_description=problem_description, appointment_date_time=mydatetime,status="New")
        return redirect('appointment_success.html')
    return render(request, 'adminMod/add_appointment.html')


def add_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            print("form.data")         
            print(form.data)
            form.save(commit=True)
        else:
            print("form.errors")
            print(form.errors)
        return redirect('appointment_success.html')
    form = AppointmentForm()
    context = {
        'form': form
    }
    return render(request, 'adminMod/add_appointment.html', context)


def edit_appointment(request, appointment_id):
    appointmentObj = get_object_or_404(appointment, id=appointment_id)
    print("objjj")
    print(appointmentObj)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointmentObj)
        if form.is_valid():
            form.save(commit=True)
        else:
            print("form.errors")
            print(form.errors)
        appointments = appointment.objects.all()
        context = {
            'appointments': appointments
        }
        return render(request, 'adminMod/admin_list.html', context)
    form = AppointmentForm(instance=appointmentObj)
    context = {
        'form': form
    }  
    return render(request, 'adminMod/edit_appointment.html', context)


def delete_appointment(request, appointment_id):
    appointmentObj = get_object_or_404(appointment, id=appointment_id)
    print(appointmentObj)
    appointmentObj.delete()
    appointments = appointment.objects.all()
    context = {
        'appointments': appointments
    }
    return render(request, 'adminMod/admin_list.html', context)


# Create your views here.
def get_home(request):
    return render(request, 'home/home.html')


def get_about(request):
    return render(request, 'home/about.html')


def get_what_we_do(request):
    return render(request, 'home/what_we_do.html')


def get_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            print("form.data")         
            print(form.data)
            form.save(commit=True)
        else:
            print("form.errors")
            print(form.errors)
        return redirect('appointment_success.html')
    form = AppointmentForm()
    context = {
        'form': form
    }
    return render(request, 'booking/book_appointment.html', context)


def get_admin_login(request):
    return render(request, 'adminMod/admin_login.html')


def get_appointment_success(request):
    return render(request, 'booking/appointment_success.html')


def do_authenticate(request):
    if request.method == 'POST':
        username = request.POST.get('user_name')
        password = request.POST.get('user_password')
        user = authenticate(username=username, password=password)
        print("user ...")
        print(user)
        if user is not None:
            """login(request, user)"""
            return redirect('adminMod.html')
        else:
            return render(request, 'adminMod/admin_not_found.html')
    return render(request, 'admin_list.html')