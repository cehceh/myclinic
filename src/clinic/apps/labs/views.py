from django.shortcuts import render, redirect
from django.urls import reverse


# Create your views here.


def add_prescription(request):
    '''  '''
    context = {

    }

    return render(request, 'labs/add_prescription.html', context)


def edit_prescription(request):
    '''  '''
    context = {

    }

    return render(request, 'labs/edit_prescription.html', context)


def table_labs(request):
    '''  '''
    context = {

    }

    return render(request, 'labs/tables.html', context)


def delete_prescription(request):
    '''  '''
    return redirect('/')
