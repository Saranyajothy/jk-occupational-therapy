"""occupationaltherapy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from adminMod.views import get_appointments, add, get_home, get_about, get_what_we_do, get_appointment, get_admin_login, get_appointment_success, do_authenticate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list', get_appointments, name='get_appointments'),
    path('adminMod.html', get_appointments, name='get_appointments'),
    path('add', add, name='add'),
    path('home', get_home, name='get_home'),
    path('', get_home, name='get_home'),
    path('about', get_about, name='get_about'),
    path('what_we_do', get_what_we_do, name='get_what_we_do'),
    path('appointment', get_appointment, name='get_appointment'),
    path('admin_login', get_admin_login, name='admin_login'),
    path('appointment_success.html', get_appointment_success, name='get_appointment_success'),
    path('do_authenticate', do_authenticate, name='do_authenticate')
]
