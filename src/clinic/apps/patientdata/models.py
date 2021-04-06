from django.db import models
from django.shortcuts import redirect
from django.urls import reverse
from django.utils import timezone
from django.utils.timezone import now 
from phonenumber_field.modelfields import PhoneNumberField

# from datetime import date
from string import ascii_uppercase, digits
# import random

current = timezone.now

# Create your models here.
class Patients(models.Model):
    name       = models.CharField(max_length=150)
    address    = models.CharField(max_length=150, blank=True, null=True)
    birth_date = models.DateField(default=now, blank=True, null=True)
    age        = models.CharField(max_length=150, blank=True, null=True)
    # (max_digits=5, decimal_places=2, default=00.00)
    # age = models.FloatField(default=00.00)
    # phone      = PhoneNumberField(default='', blank=True)
    phone      = models.CharField(max_length=150, blank=True, null=True)
    # mobile     = PhoneNumberField(blank=True, null=True)
    mobile     = models.CharField(max_length=150, blank=True, null=True)
    cardid     = models.CharField(max_length=20, blank=True, null=True)
    barcode    = models.CharField(max_length=20, blank=True, null=True)
    barimg     = models.ImageField(upload_to='patient_barcode', blank=True, null=True)

    def __str__(self):
        return "{}".format(self.name)

    def edit_patient_url(self):
        # return "/clinic/edit/{}/".format(self.id)
        return reverse('patientdata:edit_patient',
                        kwargs={'id': self.id})

