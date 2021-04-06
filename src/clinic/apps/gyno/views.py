from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.forms import inlineformset_factory
from datetime import date
from .models import (Obestetric, Menstrual, MedHistory,
                    SurHistory, GynHistory, DrugHistory)

from .forms import (ObestetricForm, MenstrualForm, MedHistoryForm,
                    SurHistoryForm, GynHistoryForm, DrugHistoryForm)

from apps.patientdata.tables import PatientsTable
from apps.patientdata.models import Patients

# Create your views here.


# Add gyn data with more than one form 
def add_gyno(request, patient_id):
    '''  '''
    if request.method == 'POST':
        obs = ObestetricForm(request.POST, prefix='obs')
        men = MenstrualForm(request.POST, prefix='men')
        if obs.is_valid() and men.is_valid():
            obs_form = obs.save(commit=False)
            obs_form.patient_id = patient_id
            # print(obs_form.patient_id)
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
                                                        'patient_id': patient_id,}))
        else:
            messages.success(request, 'Saving process failed ..!!')
            return redirect(reverse('gyno:add_gyno', kwargs={'patient_id': patient_id,}))
            print('Error')
    else:
        obs = ObestetricForm(prefix='obs')
        men = MenstrualForm(prefix='men')
       
    context = {
        # 'formset': formset,
        'obs_form': obs,
        'men_form': men,
        
    }
    return render(request, 'gyno/add_gyno.html', context)


def edit_gyno(request, obs_id: int, patient_id: int):
    '''  '''
    obestetric = Obestetric.objects.get(id=obs_id)
    menstrual = Menstrual.objects.get(obestetric_id=obs_id)
    obs = ObestetricForm(
                request.POST or None, 
                instance=obestetric, prefix='obs')
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
   
    context = {
        'obs_form': obs,
        'men_form': men,
        'obs_id': obs_id,
        'patient_id': patient_id,
    }
    return render(request, 'gyno/edit_gyno.html', context)


def add_followup_table(request):
    '''  '''
    qs = Patients.objects.all().order_by('-id')
    page_no = request.GET.get('pageno')
    if page_no == None or page_no == '' or int(page_no) == 0:
        table = PatientsTable(qs, exclude='addr, addpast, addvis')
        table.paginate(page=request.GET.get("page", 1), per_page=10)
    else:
        table = PatientsTable(qs, exclude='addr, addpast, addvis')
        table.paginate(page=request.GET.get("page", 1), per_page=page_no)
    
    context = {
        'add_followup_table':table,
    }
    return render(request, 'gyno/tables.html', context)


def delete_gyno(request, id):
    '''  '''

    context = {

    }
    return render(request, 'add_gyno.html', context)



