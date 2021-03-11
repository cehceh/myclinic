from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.forms import inlineformset_factory
from datetime import date
from .models import (Obestetric, Menstrual, MedHistory,
                    SurHistory, GynHistory, DrugHistory)

from .forms import (ObestetricForm, MenstrualForm, MedHistoryForm,
                    SurHistoryForm, GynHistoryForm, DrugHistoryForm)

# from ninja import NinjaAPI, Schema, Form
# api = NinjaAPI()


# Create your views here.


# class ObestetricIn(Schema):
#     # id: int #= models.ForeignKey(Patients, verbose_name='Patient Name:', on_delete=models.CASCADE)
#     patient: int #= models.ForeignKey(Patients, verbose_name='Patient Name:', on_delete=models.CASCADE)
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
#     patient: int    #= models.ForeignKey(Patients, on_delete=models.CASCADE)
#     obestetric: int #= models.ForeignKey(Obestetric, on_delete=models.CASCADE)
#     lmp: date = None        #= models.DateField(blank=True, null=True, verbose_name='LMP:')
#     edd: date = None        #= models.DateField(blank=True, null=True, verbose_name='EDD:')
#     ga: str         #= models.CharField(max_length=50, blank=True, null=True, verbose_name='G.A:')
#     remain: str     #= models.CharField(max_length=50, blank=True, null=True, verbose_name='Remaining Weeks:')


# @api.get("/add")
# def followup(request, name: str, followupdate: str):
#     context = {
#         'name': name, 
#         'result': ObestetricForm,
#         'followupdate': followupdate,
#     }
#     return context#{name, followupdate}

# @api.get("/gyn/add_gyno/")
# def get_gyno_form(request, obsApi: ObestetricIn = Form(...)):
#     context = {
#         'obs_form': ObestetricForm, 
#         # 'men_form': MenstrualForm,
#         'id': obsApi.id,
#         # 'patient': obsApi.patient, 'obdate': obsApi.obdate, 'gyn': obsApi.gyn,
#         # 'g': obsApi.g, 'p': obsApi.p, 'a': obsApi.a, 'nvd': obsApi.obdatenvd,
#         # 'cs': obsApi.cs, 'ld': obsApi.ld, 'lc': obsApi.lc,
#         # 'anystring': obsApi.hist,
#     }
#     return render(request, 'gyno/add_gyno.html', context)


# Add gyn data with more than one form 
# @api.api_operation(["POST", "GET"], "/gyn/add_gyno")
# @api.post("/gyn/add_gyno/")
# def add_gyno(request, obsApi: ObestetricIn = Form(...)): #, menApi: MenstrualIn = Form(...)
def add_gyno(request, patient_id):
    '''  '''
    if request.method == 'POST':
        obs = ObestetricForm(request.POST, prefix='obs')
        men = MenstrualForm(request.POST, prefix='men')
        if obs.is_valid() and men.is_valid():
            obs_form = obs.save(commit=False)
            obs_form.save()
            obs_id = obs_form.id
            pat_id = obs_form.patient_id
            obestetric = Obestetric.objects.get(id=obs_id)

            men_form = men.save(commit=False)
            men_form.obestetric_id = obs_id
            men_form.patient_id = pat_id
            men_form.save()
            
            # messages.success(request, 'Saving process done ....')
            return redirect(reverse('gyno:edit_gyno', kwargs={
                                                        'obs_id': obs_form.id,
                                                        'patient_id': pat_id,}))
        else:
            messages.success(request, 'Saving process failed ..!!')
            return redirect(reverse('gyno:add_gyno'))
            print('Error')
    else:
        obs = ObestetricForm(prefix='obs')
        men = MenstrualForm(prefix='men')
       
    context = {
        # 'formset': formset,
        'obs_form': obs,
        'men_form': men,
        # 'obsApi': obsApi,
        # 'menApi': menApi.obestetric,
        
        # 'patient': obsApi.patient, 'obdate': obsApi.obdate, 'gyn': obsApi.gyn,
        # 'g': obsApi.g, 'p': obsApi.p, 'a': obsApi.a, 'nvd': obsApi.obdatenvd,
        # 'cs': obsApi.cs, 'ld': obsApi.ld, 'lc': obsApi.lc,
        # 'anystring': obsApi.hist,
    }
    return render(request, 'gyno/add_gyno.html', context)


# @api.api_operation(["POST", "GET"], "/gyn/edit_gyno/{obs_id}/{patient_id}")
def edit_gyno(request, obs_id: int, patient_id: int):
    '''  '''
    obestetric = Obestetric.objects.get(id=obs_id)
    menstrual = Menstrual.objects.get(obestetric_id=obs_id)
    obs = ObestetricForm(request.POST or None, 
                            instance=obestetric, 
                            prefix='obs')
    men = MenstrualForm(request.POST or None, instance=menstrual, prefix='men')
    if obs.is_valid() and men.is_valid():
        obs_form = obs.save(commit=False)
        obs_form.save()
        obs_id = obs_form.id
        pat_id = obs_form.patient_id
        
        men_form = men.save(commit=False)
        men_form.obestetric_id = obs_id
        men_form.patient_id = pat_id
        men_form.save()

        messages.success(request, 'Saving changes done ....')
        return redirect(reverse('gyno:edit_gyno', kwargs={
                                                        'obs_id': obs_id,
                                                        'patient_id': pat_id,}))
    # else:
    #     messages.success(request, 'Saving changes failed ..!!')
        # return redirect(reverse('gyno:edit_gyno', kwargs={'obs_id': obs_id}))
        # return redirect('gyno:add_gyno')
    context = {
        'obs_form': obs,
        'men_form': men,
        'obs_id': obs_id,
        'patient_id': patient_id,
    }
    return render(request, 'gyno/edit_gyno.html', context)


def table_gyno(request):
    '''  '''

    context = {

    }
    return render(request, 'gyno/tables.html', context)


def delete_gyno(request, id):
    '''  '''

    context = {

    }
    return render(request, 'add_gyno.html', context)



