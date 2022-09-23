from django.shortcuts import render,redirect
from .models import adminMod_appointment


# Create your views here.
def get_appointments(request):
    appointments = adminMod_appointment.objects.all()

    context = {
        'appointments': appointments
    }

    return render(request, 'adminMod/adminMod.html', context)


def add_appointment(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = "Sample address"
        email = "sample@gmail.com"
        mobile_ext = request.POST.get('mobile_ext')
        mobile = request.POST.get('mobile')
        problem_description = request.POST.get('symptoms')
        date = request.POST.get('date')
        adminMod_appointment.objects.create(firstname=first_name, lastname=last_name, 
        address=address, email=email, mobile_ext=mobile_ext, mobile=mobile, problem_description=problem_description, appointment_date_time=date)
    return redirect('adminMod.html')

    return render(request, 'adminMod/add_appointment.html')
