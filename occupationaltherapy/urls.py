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
# from adminMod.views import get_appointments, add, get_home, get_about, get_what_we_do, get_appointment, get_admin_login, get_appointment_success, do_authenticate
from adminMod import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('list', get_appointments, name='get_appointments'),
#     path('adminMod.html', get_appointments, name='get_appointments'),
#     path('add', add, name='add'),
#     path('home', get_home, name='get_home'),
#     path('', get_home, name='get_home'),
#     path('about', get_about, name='get_about'),
#     path('what_we_do', get_what_we_do, name='get_what_we_do'),
#     path('appointment', get_appointment, name='get_appointment'),
#     path('admin_login', get_admin_login, name='admin_login'),
#     path('appointment_success.html', get_appointment_success, name='get_appointment_success'),
#     path('do_authenticate', do_authenticate, name='do_authenticate')
# ]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('list', views.get_appointments, name='get_appointments'),
    path('adminMod.html', views.get_appointments, name='get_appointments'),
    # path('add', views.add, name='add'),
    path('add', views.add_appointment, name='add'),
    path('edit/<appointment_id>', views.edit_appointment, name='edit'),
    path('delete/<appointment_id>', views.delete_appointment, name='edit'),
    path('home', views.get_home, name='get_home'),
    path('', views.get_home, name='get_home'),
    path('about', views.get_about, name='get_about'),
    path('what_we_do', views.get_what_we_do, name='get_what_we_do'),
    path('appointment', views.get_appointment, name='get_appointment'),
    path('admin_login', views.get_admin_login, name='admin_login'),
    path('appointment_success.html', views.get_appointment_success, name='get_appointment_success'),
    path('do_authenticate', views.do_authenticate, name='do_authenticate')
]
