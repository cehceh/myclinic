from django.shortcuts import render, redirect
from django.urls import reverse




# Create your views here.

def add_gyno(request):
    '''  '''

    context = {

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


