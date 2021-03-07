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
    if request.method == 'POST':
        obs = ObestetricForm(request.POST, prefix='obs')
        men = MenstrualForm(request.POST, prefix='men')
        # med = MedHistoryForm(request.POST, prefix='med')
        # sur = SurHistoryForm(request.POST, prefix='sur')
        # gyn = GynHistoryForm(request.POST, prefix='gyn')
        # drg = DrugHistoryForm(request.POST, prefix='drg')
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
            
            # med_form = med.save(commit=False)
            # med_form.obestetric_id = obs_id
            # med_form.patient_id = pat_id
            # med_form.save()

            # sur_form = sur.save(commit=False)
            # sur_form.obestetric_id = obs_id
            # sur_form.patient_id = pat_id
            # sur_form.save()

            # gyn_form = gyn.save(commit=False)
            # gyn_form.obestetric_id = obs_id
            # gyn_form.patient_id = pat_id
            # gyn_form.save()

            # drg_form = drg.save(commit=False)
            # drg_form.obestetric_id = obs_id
            # drg_form.patient_id = pat_id
            # drg_form.save()

            # messages.success(request, 'Saving process done ....')
            return redirect(reverse('gyno:edit_gyno', kwargs={
                                                        'obs_id': obs_form.id,
                                                        'patient_id': pat_id,}))
        else:
            messages.success(request, 'Saving process failed ..!!')
            return redirect(reverse('gyno:add_gyno'))
            print('Error')
    else:
        # formset = ObestetricFormSet()
        obs = ObestetricForm(prefix='obs')
        men = MenstrualForm(prefix='men')
        # med = MedHistoryForm(prefix='med')
        # sur = SurHistoryForm(prefix='sur')
        # gyn = GynHistoryForm(prefix='gyn')
        # drg = DrugHistoryForm(prefix='drg')
    
    context = {
        # 'formset': formset,
        'obs_form': obs,
        'men_form': men,
        # 'med_form': med,
        # 'sur_form': sur,
        # 'gyn_form': gyn,
        # 'drg_form': drg,
    }
    return render(request, 'gyno/add_gyno.html', context)


def edit_gyno(request, obs_id, patient_id):
    '''  '''
    obestetric = Obestetric.objects.get(id=obs_id)
    menstrual = Menstrual.objects.get(obestetric_id=obs_id)
    obs = ObestetricForm(request.POST or None, 
                            instance=obestetric, 
                            # data={
                            #     'patient_id': patient_id,
                            # },
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


