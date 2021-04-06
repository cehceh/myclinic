from django.db import models
from apps.patientdata.models import Patients


# Create your models here.

class Obestetric(models.Model):
    patient = models.ForeignKey(Patients, blank=True, null=True, verbose_name='Patient Name:', on_delete=models.CASCADE)
    obdate  = models.DateField(blank=True, null=True, verbose_name='Follow Up Date:')
    gyn     = models.BooleanField(verbose_name='Gyn:', default=False)
    g       = models.IntegerField(default=0, blank=True, null=True, verbose_name='G:')
    p       = models.IntegerField(default=0, blank=True, null=True, verbose_name='P:')
    a       = models.IntegerField(default=0, blank=True, null=True, verbose_name='A:')
    nvd     = models.BooleanField(default=False, verbose_name='NVD:')
    cs      = models.BooleanField(default=False, verbose_name='CS:')
    ld      = models.CharField(max_length=150, blank=True, null=True, verbose_name='LD:')
    lc      = models.CharField(max_length=150, blank=True, null=True, verbose_name='LC:')
    hist    = models.TextField(max_length=250, verbose_name='History of previous obestetric complication(if any):', blank=True, null=True)

    def __str__(self):
        return "{}".format(self.id)


class Menstrual(models.Model):
    patient    = models.ForeignKey(Patients, blank=True, null=True, on_delete=models.CASCADE)
    obestetric = models.ForeignKey(Obestetric, blank=True, null=True, on_delete=models.CASCADE)
    lmp        = models.DateField(blank=True, null=True, verbose_name='LMP:')
    edd        = models.DateField(blank=True, null=True, verbose_name='EDD:')
    ga         = models.CharField(max_length=50, blank=True, null=True, verbose_name='G.A:')
    remain     = models.CharField(max_length=50, blank=True, null=True, verbose_name='Remaining Weeks:')

    def __str__(self):
        return "{}".format(self.obestetric)


class MedHistory(models.Model):
    patient    = models.ForeignKey(Patients, blank=True, null=True, on_delete=models.CASCADE)
    obestetric = models.ForeignKey(Obestetric, blank=True, null=True, on_delete=models.CASCADE)
    name       = models.CharField(max_length=150, blank=True, null=True, verbose_name='Medical History:')

    def __str__(self):
        return "{}".format(self.name)



class SurHistory(models.Model):
    patient    = models.ForeignKey(Patients, blank=True, null=True, on_delete=models.CASCADE)
    obestetric = models.ForeignKey(Obestetric, blank=True, null=True, on_delete=models.CASCADE)
    name       = models.CharField(max_length=150, verbose_name='Surgical History:', blank=True, null=True)
    
    def __str__(self):
        return "{}".format(self.name)


class GynHistory(models.Model):
    patient    = models.ForeignKey(Patients, blank=True, null=True, on_delete=models.CASCADE)
    obestetric = models.ForeignKey(Obestetric, blank=True, null=True, on_delete=models.CASCADE)
    name       = models.CharField(max_length=150, blank=True, null=True, verbose_name='Gynecological History:')
    
    def __str__(self):
        return "{}".format(self.name)


class DrugHistory(models.Model):
    patient    = models.ForeignKey(Patients, blank=True, null=True, on_delete=models.CASCADE)
    obestetric = models.ForeignKey(Obestetric, blank=True, null=True, on_delete=models.CASCADE)
    name       = models.CharField(max_length=150, blank=True, null=True, verbose_name='Drug History:')
    
    def __str__(self):
        return "{}".format(self.name)