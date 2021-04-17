from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.db.models import Max
from django.db import connection, transaction
from django.contrib import messages
from datetime import datetime, date
# from django.contrib.postgres.search import SearchVector

from apps.patientdata.forms import PatientsForm
from apps.patientdata.models import Patients
from apps.visits.forms import VisitsForm
from apps.visits.models import Visits
from apps.patientdata.tables import PatientsTable
from apps.visits.tables import VisitsTable


def calculate_day_income(request):
    today = date.today()#datetime.now()

    day_income = Visits.objects.filter(visitdate__year=today.year, visitdate__month=today.month, visitdate__day=today.day)
    day_table = VisitsTable(day_income, exclude='addpresent')
    day_table.paginate(page=request.GET.get("page", 1), per_page=3)
    # print(day_income)
    
    context = {
            'day_table': day_table,
    }
    return render(request, 'reports/day_table.html', context)


def calculate_month_income(request):
    today = date.today()#datetime.now()
    month_income = Visits.objects.filter(visitdate__year=today.year, visitdate__month=today.month)
    month_table = VisitsTable(month_income, exclude='addpresent')
    month_table.paginate(page=request.GET.get("page", 1), per_page=10)

    context = {
        'month_table': month_table,
    }
    return render(request, 'reports/month_table.html', context)

def calculate_year_income(request):
    today = date.today()#datetime.now()
    # income = Visits.objects.all()
    # table = VisitsTable(income)
    # table.paginate(page=request.GET.get('page', 1), per_page=10)

    year_income = Visits.objects.filter(visitdate__year=today.year).order_by('-id')
    year_table = VisitsTable(year_income, exclude='addpresent')
    year_table.paginate(page=request.GET.get("page", 1), per_page=10)
    
    context = {
        'year_table': year_table,
    }
    return render(request, 'reports/year_table.html', context)



def calculate_income(request, year):
    today = date.today()#datetime.now()
    day = today.day
    month = today.month
    year = today.year
    # income = Visits.objects.all()
    # table = VisitsTable(income)
    # table.paginate(page=request.GET.get('page', 1), per_page=10)
    # if day is not None and month is not None and year is not None:
    #     day_income = Visits.objects.filter(visitdate__year=today.year, visitdate__month=today.month, visitdate__day=today.day)
    #     table = VisitsTable(day_income)
    #     table.paginate(page=request.GET.get("page", 1), per_page=2)
    #     return redirect(reverse('clinic:day_income', args=(today.day, today.month, today.year)))
    # elif month is not None and year is not None:
    #     month_income = Visits.objects.filter(visitdate__year=today.year, visitdate__month=today.month)
    #     table = VisitsTable(month_income)
    #     table.paginate(page=request.GET.get("page", 1), per_page=3)
    #     return redirect(reverse('clinic:month_income', args=(today.month, today.year)))
    # if year != None:
    cal_year = Visits.objects.values('visitdate').filter(visitdate__year=year).first()
    year_value = cal_year['visitdate']
    # print(cal_year, year_value)
    year_income = Visits.objects.filter(visitdate__year=today.year).order_by('-id')
    table = VisitsTable(year_income, exclude='addpresent')
    table.paginate(page=request.GET.get("page", 1), per_page=5)
    return redirect('/clinic/income/year/'+ str(year_value.year) +'/')
    
    context = {
        'income_table': table,
    }
    return render(request, 'tables.html', context)
