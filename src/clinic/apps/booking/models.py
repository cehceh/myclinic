from django.db import models
from django.shortcuts import reverse 
from apps.patientdata.models import Patients

# Create your models here.


class Appointment(models.Model):
    patient = models.ForeignKey(Patients, 
                            blank=True, null=True, 
                            on_delete=models.CASCADE)
    # patient = models.CharField(max_length=100)
    bookdate = models.DateField()
    starttime = models.CharField(max_length=20, null=True, blank=True)
    endtime = models.CharField(max_length=20, null=True, blank=True)
    booknum = models.IntegerField(default=0)

    def __str__(self):
        return "{}".format(self.id)

    # def get_absolute_url(self):
    #     return reverse('booking:edit_book',
    #                     kwargs={'id': self.id})