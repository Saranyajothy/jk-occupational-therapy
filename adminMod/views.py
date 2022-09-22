from django.shortcuts import render
from .models import adminMod_appointment

# Create your views here.
def get_appointments(request):
    appointments = adminMod_appointment.objects.all()

    context = {
        'appointments': appointments
    }

    return render(request, 'adminMod/adminMod.html', context)
