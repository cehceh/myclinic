from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import LabVisitForm, LabFollowupForm
from .models import LabVisit, LabFollowup

# Create your views here.

def add_lab_visit(request, patient_id, visit_id):
    '''  '''
    if request.method == 'POST':
        form = LabVisitForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            lab_form = form.save(commit=False)
            lab_form.visit = visit_id
            lab_form.patient = patient_id
            lab_form.save()
    else:
        form = LabVisitForm()

    context = {

    }

    return render(request, 'labs/add_lab_visit.html', context)


def add_lab_followup(request, patient_id, followup_id):
    '''  '''
    if request.method == 'POST':
        form = LabFollowupForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            lab_form = form.save(commit=False)
            lab_form.followup = followup_id
            lab_form.patient = patient_id

            lab_form.save()
    context = {

    }

    return render(request, 'labs/add_lab_followup.html', context)


def edit_lab_visit(request, lab_id, patient_id, visit_id):
    '''  '''
    qs = LabVisit.objects.get(id=lab_id)
    form = LabVisitForm(request.POST or None, request.FILES or None, instance=qs)
    context = {

    }

    return render(request, 'labs/edit_lab_visit.html', context)


def edit_lab_followup(request, lab_id, patient_id, followup_id):
    '''  '''
    qs = LabFollowup.objects.get(id=lab_id)
    form = LabVisitForm(request.POST or None, request.FILES or None, instance=qs)
    context = {

    }

    return render(request, 'labs/edit_lab_followup.html', context)


def table_labs(request):
    '''  '''
    context = {

    }

    return render(request, 'labs/tables.html', context)


def delete_lab_visit(request):
    '''  '''
    return redirect('/')

def delete_lab_followup(request):
    '''  '''
    return redirect('/')
