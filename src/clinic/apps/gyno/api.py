from datetime import date
from django.shortcuts import get_object_or_404
from apps.patientdata.models import Patients
from .models import (Obestetric, Menstrual, MedHistory,
                    SurHistory, GynHistory, DrugHistory)
from .forms import (ObestetricForm, MenstrualForm, MedHistoryForm,
                    SurHistoryForm, GynHistoryForm, DrugHistoryForm)

from ninja import NinjaAPI, Schema, Form
api = NinjaAPI()


# Create your views here.
# @api.get("/employees/{employee_id}", response=EmployeeOut)
# def get_employee(request, employee_id: int):
#     employee = get_object_or_404(Employee, id=employee_id)
#     return employee
class ObestetricIn(Schema):
    id: int  #= models.ForeignKey(Patients, verbose_name='Patient Name:', on_delete=models.CASCADE)
    patient_id: int = None #= models.ForeignKey(Patients, verbose_name='Patient Name:', on_delete=models.CASCADE)
    obdate: date  # = models.DateField(blank=True, null=True, verbose_name='Follow Up Date:')
    gyn: bool     #= models.BooleanField(verbose_name='Gyn:', default=False)
    g: int       #= models.IntegerField(default=0, blank=True, null=True, verbose_name='G:')
    p: int      # = models.IntegerField(default=0, blank=True, null=True, verbose_name='P:')
    a: int      # = models.IntegerField(default=0, blank=True, null=True, verbose_name='A:')
    nvd: bool  #     = models.BooleanField(default=False, verbose_name='NVD:')
    cs: bool   #= models.BooleanField(default=False, verbose_name='CS:')
    ld: str    # = models.CharField(max_length=150, blank=True, null=True, verbose_name='LD:')
    lc: str    #= models.CharField(max_length=150, blank=True, null=True, verbose_name='LC:')
    hist: str


class MenstrualIn(Schema):
    id: int
    patient_id: int = None   #= models.ForeignKey(Patients, on_delete=models.CASCADE)
    obestetric_id: int = None #= models.ForeignKey(Obestetric, on_delete=models.CASCADE)
    lmp: date = None        #= models.DateField(blank=True, null=True, verbose_name='LMP:')
    edd: date = None        #= models.DateField(blank=True, null=True, verbose_name='EDD:')
    ga: str         #= models.CharField(max_length=50, blank=True, null=True, verbose_name='G.A:')
    remain: str     #= models.CharField(max_length=50, blank=True, null=True, verbose_name='Remaining Weeks:')


class ObesMenRelation(Schema):
    id: int
    obestetric_id: int = None #= models.ForeignKey(Obestetric, on_delete=models.CASCADE)
    patient_id: int = None #= models.ForeignKey(Patients, verbose_name='Patient Name:', on_delete=models.CASCADE)
    obestetric__obdate: date = None # = models.DateField(blank=True, null=True, verbose_name='Follow Up Date:')
    obestetric__gyn: bool = False    #= models.BooleanField(verbose_name='Gyn:', default=False)
    obestetric__g: int = None     #= models.IntegerField(default=0, blank=True, null=True, verbose_name='G:')
    obestetric__p: int = None   # = models.IntegerField(default=0, blank=True, null=True, verbose_name='P:')
    obestetric__a: int = None   # = models.IntegerField(default=0, blank=True, null=True, verbose_name='A:')
    obestetric__nvd: bool = False  #     = models.BooleanField(default=False, verbose_name='NVD:')
    obestetric__cs: bool = False  #= models.BooleanField(default=False, verbose_name='CS:')
    obestetric__ld: str = "string"  # = models.CharField(max_length=150, blank=True, null=True, verbose_name='LD:')
    obestetric__lc: str = "string"  #= models.CharField(max_length=150, blank=True, null=True, verbose_name='LC:')
    obestetric__hist: str 
    # obestetric__id: int  #= models.ForeignKey(Obestetric, on_delete=models.CASCADE)
    lmp: date = None        #= models.DateField(blank=True, null=True, verbose_name='LMP:')
    edd: date = None        #= models.DateField(blank=True, null=True, verbose_name='EDD:')
    ga: str  = ""      #= models.CharField(max_length=50, blank=True, null=True, verbose_name='G.A:')
    remain: str = ""


@api.get("/gyn/get/obestetric/id/{obs_id}/", response=ObestetricIn)
def followup(request, obs_id: int):
    obs = get_object_or_404(Obestetric, id=obs_id)
    return obs #context #{name, followupdate}


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


from typing import List # Important import to get all objects without error
@api.get('/all/obestetric/and/menstrual/', response=List[ObesMenRelation])
def get_obsmen(request):
    obs = Obestetric.objects.all().order_by('-id')
    men = Menstrual.objects.select_related('obestetric')
                            # .filter().order_by('-gyno_obestetric.obdate')
    # men = Menstrual.objects.all().filter(obestetric__in=obs)
    print(men)
    return men

@api.get('/all/obestetric/', response=List[ObestetricIn])
def get_obestetric(request):
    obs = Obestetric.objects.all().order_by('-id')
    return obs

@api.get('/all/Menstrual/', response=List[MenstrualIn])
def get_menstrual(request):
    obs = Menstrual.objects.all().order_by('-id')
    return obs




    # patient: int, obdate: date, gyn: bool,
    # g: int, p: int, a: int, nvd: bool, cs: bool,
    # ld:str, lc: str, hist: str):
    # context = {
    #     ''
    #     # 'patient': patient, 'obdate': obdate, 'gyn': gyn,
    #     # 'g': g, 'p': p, 'a': a, 'nvd': nvd, 'cs': cs,
    #     # 'ld': ld, 'lc': lc, 'anystring': hist,
    # }
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
