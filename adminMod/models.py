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

    
class appointment(models.Model):
    firstname = models.CharField(max_length=50, null=False, blank=False)
    lastname = models.CharField(max_length=50, null=False, blank=False)
    address = models.CharField(max_length=300, null=False,blank=False)
    email = models.CharField(max_length=100, null=False,blank=False)
    mobile_ext = models.CharField(max_length=3, null=False,blank=False)
    mobile = models.IntegerField(null=False, blank=False)
    symptoms = models.TextField(max_length=500, null=False,blank=False)
    date = models.DateField(max_length=50, null=False,blank=False)
    time = models.TimeField(max_length=50, null=False,blank=False)

    def __str__(self):
        return self.firstname

class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False)