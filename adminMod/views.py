from django.shortcuts import render,redirect
from .models import adminMod_appointment, Item
from datetime import datetime
from django.db import models
from django.utils.dateparse import parse_date, parse_time
from .forms import ItemForm


# Create your views here.
def get_appointments(request):
    appointments = adminMod_appointment.objects.all()

    context = {
        'appointments': appointments
    }

    return render(request, 'adminMod/adminMod.html', context)


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

    
def edit_item(request,item_id):
    item = get_object_or_404(Item, id=item_id)
    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    from django.shortcuts import render, redirect, get_object_or_404


    return render(request, 'todo/edit_item.html', context)


# Create your views here.
def get_home(request):
    return render(request, 'adminMod/home.html')


def get_about(request):
    return render(request, 'adminMod/about.html')


def get_what_we_do(request):
    return render(request, 'adminMod/what_we_do.html')


def get_appointment(request):
    return render(request, 'adminMod/appointment.html')


def get_assets(request):
    return render(request, 'adminMod/assets')


def get_admin_login(request):
    return render(request, 'adminMod/admin_login.html')


def get_appointment_success(request):
    return render(request, 'adminMod/appointment_success.html')