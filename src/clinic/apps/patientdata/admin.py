from django.contrib import admin
from apps.patientdata.models import Patients

admin.site.register(Patients)

# Register your models here.
# 
class PatientsAdmin(admin.ModelAdmin):
    pass 

