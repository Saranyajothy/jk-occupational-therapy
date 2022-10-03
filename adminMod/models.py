from django.db import models
# Create your models here.
class adminMod_appointment(models.Model):
    firstname = models.CharField(max_length=50, null=False, blank=False)
    lastname = models.CharField(max_length=50, null=False, blank=False)
    address = models.CharField(max_length=300, null=False,blank=False)
    email = models.CharField(max_length=100, null=False,blank=False)
    mobile_ext = models.CharField(max_length=5,null=False,blank=False)
    mobile = models.IntegerField(null=False,blank=False)
    complaint_description = models.TextField(max_length=500,null=False,blank=False)
    appointment_date_time = models.DateTimeField(max_length=50,null=False,blank=False)
    status = models.CharField(max_length=20,null=False,blank=False)

    def __str__(self):
        return self.firstname


class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False)


# class appointment(FormView):
#     form_class = AvailabilityForm
#     template_name = "add_appointment.html"

#     def form_valid(self, form):
#         data = form.cleaned_data
#         bookingList = appointment.objects.filter()
        
#         for booking in bookingList:
#             if booking.start > data["end_time"] or booking.end < data["start_time"]:
#                 booking=appointment.objects.create(
#                     name=data["name"], 
#                     start=data["start_time"],
#                     end=data["end_time"]
#                     )
#                 booking.save()
#                 print(booking.start)
#                 print(data["start_time"])
#                 return HttpResponse("can be booked")
#             else:
#                 print(booking.start )
#                 print(data["start_time"])
#                 return HttpResponse("Cant be booked")