from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.forms import inlineformset_factory

from .models import (Obestetric, Menstrual, MedHistory,
                    SurHistory, GynHistory, DrugHistory)

from .forms import (ObestetricForm, MenstrualForm, MedHistoryForm,
                    SurHistoryForm, GynHistoryForm, DrugHistoryForm)



# Create your views here.

# Add gyn data with more than one form 
def add_gyno(request):
    '''  '''
    # ObestetricFormSet = inlineformset_factory(Obestetric, Menstrual, MedHistory,    
    #                     fields=('patient','gyn','g','p','a','nvd','cs',
    #                             'ld','lc','hist','lmp','edd','ga','remain','name')) # SurHistory, GynHistory, DrugHistory,
    if request.method == 'POST':
        # formset = ObestetricFormSet(request.POST or None)
        obs = ObestetricForm(request.POST, prefix='obs')
        men = MenstrualForm(request.POST, prefix='men')
        med = MedHistoryForm(request.POST, prefix='med')
        sur = SurHistoryForm(request.POST, prefix='sur')
        gyn = GynHistoryForm(request.POST, prefix='gyn')
        drg = DrugHistoryForm(request.POST, prefix='drg')
        if obs.is_valid() and men.is_valid() and med.is_valid() and sur.is_valid() and gyn.is_valid() and drg.is_valid():
        # if formset.is_valid():
            # formset.save()
            obs_form = obs.save(commit=False)
            obs_form.save()
            obs_id = obs_form.id
            pat_id = obs_form.patient_id
            
            men_form = men.save(commit=False)
            men_form.obestetric_id = obs_id
            men_form.patient_id = pat_id
            men_form.save()
            # men_id = request.POST.get('obestetric_id')
            # med.cleaned_data['obestetric_id'] = obs_id
            med_form = med.save(commit=False)
            med_form.obestetric_id = obs_id
            med_form.patient_id = pat_id
            med_form.save()

            # sur.cleaned_data['obestetric_id'] = obs_form.id
            sur_form = sur.save(commit=False)
            sur_form.obestetric_id = obs_id
            sur_form.patient_id = pat_id
            sur_form.save()

            # gyn.cleaned_data['obestetric_id'] = obs_form.id
            gyn_form = gyn.save(commit=False)
            gyn_form.obestetric_id = obs_id
            gyn_form.patient_id = pat_id
            gyn_form.save()

            # drg.cleaned_data['obestetric_id'] = obs_form.id
            drg_form = drg.save(commit=False)
            drg_form.obestetric_id = obs_id
            drg_form.patient_id = pat_id
            drg_form.save()

            messages.success(request, 'Saving process done ....')
            return redirect('gyno:add_gyno')
        else:
            messages.success(request, 'Saving process failed ..!!')
            print('Error')
    else:
        # formset = ObestetricFormSet()
        obs = ObestetricForm(prefix='obs')
        men = MenstrualForm(prefix='men')
        med = MedHistoryForm(prefix='med')
        sur = SurHistoryForm(prefix='sur')
        gyn = GynHistoryForm(prefix='gyn')
        drg = DrugHistoryForm(prefix='drg')
    
    context = {
        # 'formset': formset,
        'obs_form': obs,
        'men_form': men,
        'med_form': med,
        'sur_form': sur,
        'gyn_form': gyn,
        'drg_form': drg,
    }
    return render(request, 'gyno/add_gyno.html', context)


def edit_gyno(request, id):
    '''  '''

    context = {

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


