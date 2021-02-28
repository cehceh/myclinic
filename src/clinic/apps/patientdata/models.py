from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.timezone import now 

# from datetime import date
from string import ascii_uppercase, digits
# import random

current = timezone.now

# Create your models here.
class Patients(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150, blank=True, null=True)
    # birth_date = models.CharField(max_length=15, blank=True, null=True)
    birth_date = models.DateField(default=now, blank=True, null=True)
    age = models.DecimalField(max_digits=5, decimal_places=2, default=00.00)
    # age = models.FloatField(default=00.00)
    phone = models.CharField(max_length=150, blank=True, null=True)
    mobile = models.CharField(max_length=150, blank=True, null=True)
    cardid= models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.name)

    def get_absolute_url(self):
        # return "/clinic/edit/{}/".format(self.id)
        return reverse('patientdata:edit_patient', kwargs={'id': self.id})

