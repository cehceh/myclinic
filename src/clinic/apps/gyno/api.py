from datetime import date
from apps.patientdata.models import Patients
from .models import (Obestetric, Menstrual, MedHistory,
                    SurHistory, GynHistory, DrugHistory)
from .forms import (ObestetricForm, MenstrualForm, MedHistoryForm,
                    SurHistoryForm, GynHistoryForm, DrugHistoryForm)

from ninja import NinjaAPI, Schema, Form
api = NinjaAPI()


# Create your views here.


@api.get("/gyn/add_gyno/")
def followup(request,  
            patient: int, obdate: date, gyn: bool,
            g: int, p: int, a: int, nvd: bool, cs: bool,
            ld:str, lc: str, hist: str):
    context = {
        'patient': patient, 'obdate': obdate, 'gyn': gyn,
        'g': g, 'p': p, 'a': a, 'nvd': nvd, 'cs': cs,
        'ld': ld, 'lc': lc, 'anystring': hist,
    }
    return context #{name, followupdate}



# class ObestetricIn(Schema):
#     patient: int = None #= models.ForeignKey(Patients, verbose_name='Patient Name:', on_delete=models.CASCADE)
#     obdate: date = None # = models.DateField(blank=True, null=True, verbose_name='Follow Up Date:')
#     gyn: bool     #= models.BooleanField(verbose_name='Gyn:', default=False)
#     g: int       #= models.IntegerField(default=0, blank=True, null=True, verbose_name='G:')
#     p: int      # = models.IntegerField(default=0, blank=True, null=True, verbose_name='P:')
#     a: int      # = models.IntegerField(default=0, blank=True, null=True, verbose_name='A:')
#     nvd: bool  #     = models.BooleanField(default=False, verbose_name='NVD:')
#     cs: bool   #= models.BooleanField(default=False, verbose_name='CS:')
#     ld: str    # = models.CharField(max_length=150, blank=True, null=True, verbose_name='LD:')
#     lc: str    #= models.CharField(max_length=150, blank=True, null=True, verbose_name='LC:')
#     hist: str

# class MenstrualIn(Schema):
#     # patient: int = None   #Patients.objects.all() = models.ForeignKey(Patients, on_delete=models.CASCADE)
#     obestetric: int #= models.ForeignKey(Obestetric, on_delete=models.CASCADE)
#     lmp: date = None        #= models.DateField(blank=True, null=True, verbose_name='LMP:')
#     edd: date = None        #= models.DateField(blank=True, null=True, verbose_name='EDD:')
#     ga: str         #= models.CharField(max_length=50, blank=True, null=True, verbose_name='G.A:')
#     remain: str     #= models.CharField(max_length=50, blank=True, null=True, verbose_name='Remaining Weeks:')


@api.post("/gyn/add_gyno/")
def create_gyno(request,  
                patient: int, obdate: date, gyn: bool,
                g: int, p: int, a: int, nvd: bool, cs: bool,
                ld:str, lc: str, hist: str):
    context = {
        'patient': patient, 'obdate': obdate, 'gyn': gyn,
        'g': g, 'p': p, 'a': a, 'nvd': nvd, 'cs': cs,
        'ld': ld, 'lc': lc, 'anystring': hist,     
    }
    return context

 # obestetric = Obestetric.objects.create(**payload.dict()) # payload: ObestetricIn,
    # 'id': obestetric.id, 
        # 'patient':obestetric.patient_id,


# Add gyn data with more than one form 
# @api.api_operation(["POST", "GET"], "/gyn/add_gyno")
# @api.post("/gyn/add_gyno")
# def add_gyno(request, obs: ObestetricIn = Form(...), men: MenstrualIn = Form(...)):
# # def add_gyno(request):
#     '''  '''
#     obestetric = Obestetric.objects.all()

#     context = {
#         # 'formset': formset,
#         'obs_form': obs,
#         'men_form': men,
#     }
#     return render(request, 'gyno/add_gyno.html', context)

