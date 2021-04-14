from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.db.models import Q, Sum, Max, Count
from django.db import connection, transaction
from django.contrib import messages
from datetime import date
# from django.db.models import Q
import os
import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image
# from django.contrib.postgres.search import SearchVector
from .forms import PatientsForm
from .models import Patients
from .tables import PatientsTable

from apps.pasthistory.models import PastHistory
from apps.presenthistory.models import PresentHistory
from apps.visits.models import Visits
from apps.visits.tables import VisitsTable


#
def save_patient(request):
    """ Collecting data for patients function to save patient data to database """ 
    if request.method == 'POST':
        form = PatientsForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            barcode_value = request.POST.get('barurl')
            if barcode_value == None or barcode_value == '':
                messages.success(request, 'Create barcode without value is not valid')
            elif barcode_value != None:
                qr = pyqrcode.create(barcode_value)
                name = request.POST.get('name')
                file_path = 'media_root/patients/' + str(name) + '.png'
                # print(file_path)
                match = Patients.objects.filter(name=name).exists()
                if not os.path.exists(file_path) and not match:
                    qr.png('media_root/patients/' + str(name) + '.png', scale=10)
                    save_form = form.save(commit=False)
                    save_form.barimg = 'patients/' + str(name) + '.png' 
                    save_form.barurl = barcode_value
                    save_form.save()
                    pat_id = save_form.id
                    Visits.objects.create(patient_id=pat_id, visitdate=date.today(),
                                    complain="any comp", sign="any sign", 
                                    amount=0, intervention="any intervention")
                    messages.success(request, 'Saving process done ... ')
                    return redirect('patientdata:table_patient')
                else:
                    messages.success(request, 'Barcode is already exists or Patient name is repeated')
                    return redirect(reverse('patientdata:save_patient'))
    else:
        form = PatientsForm()

    lastid = Patients.objects.values('id').last()
    patid = lastid['id'] + 1
    # print(patid)
    label2 = "Save"
    context = {
        'savepatform': form,
        'lastid': patid,
        # 'button_lable': label,
        'lable2': label2,

    }
    return render(request, 'patientdata/save_patient.html', context)


def edit_patient(request, id): # Making Update to a Patient
    qs = Visits.objects.filter(patient=id).order_by('-id')
    # print('qs = '+str(qs))
    # match_presenthist = PresentHistory.objects.filter(patient=id, visit=1).exists()
    table = VisitsTable(qs, exclude='patient, addpresent')
    table.paginate(page=request.GET.get("page", 1), per_page=10)

    query = Patients.objects.get(id=id)  # get(birth_date=birth_date)
    patient = Patients.objects.values('id').filter(id=id).first()
    barcode = Patients.objects.values('barcode').filter(id=id).first()
    # patient = Patients.objects.filter(id=id)
    patient_id = patient['id']
    bar = barcode['barcode']
    # print(query, patient)
    match_pasthist = PastHistory.objects.filter(patient=id).exists()
    # if match_pasthist:
    #     pasthist = PastHistory.objects.values('id').filter(patient=patient_id).first()
    
    form = PatientsForm(request.POST or None, request.FILES or None, instance=query)
    if form.is_valid():
        save_form= form.save(commit=False)
        save_form.save()
        name = save_form.name
        card = save_form.cardid 
        dup_name = Patients.objects\
                        .values('name')\
                        .annotate(ncount=Count('name'))\
                        .filter(name=name, ncount__gt=1)
        records = Patients.objects\
                        .filter(name__in=[item['name'] for item in dup_name])
        # print('rec_edit = '+ str(records) + str(name))#(dup_name, records)
        rec = [item.name for item in records]
        reco = any(rec.count(element) > 1 for element in rec)
        print('patname= '+str(name), 'rec_edit= '+str(rec), 'dupname_edit= ' +str(dup_name),reco)
        
        # check duplicate for cardid
        dup_num = Patients.objects \
                            .values('cardid') \
                            .annotate(bcount=Count('cardid')) \
                            .filter(cardid=card, bcount__gt=1)
        records_num = Patients.objects.filter(cardid__in=[item['cardid'] for item in dup_num])
        # print('recnum_edit = '+ str(records_num) + str(num))#(dup_name, records)
        rec_num = [item.cardid for item in records_num]
        reco_num = any(rec_num.count(element) > 1 for element in rec_num)
        # print(rec_num, 'reco_num= ' + str(reco_num))
        
        if reco or reco_num:
            if reco:
                messages.success(request, 'Patient (' +str(name)+ ') is already exists change the name ..!')
                return redirect(reverse('patientdata:edit_patient', kwargs={'id': id}))
            elif reco_num:
                messages.success(request, 'Card ID is already exists !, It must not be duplicated')
                return redirect(reverse('patientdata:edit_patient', kwargs={'id':id}))
        else:
            return redirect(reverse('patientdata:table_patient'))
    
    # lastid = Patients.objects.values('id').last()
    # patid = lastid['id'] + 1
    context = { 
        'patient': patient,
        'patient_id': patient_id,
        'editpatform': form,
        'query': query,
        'barcode': bar,
        'match_pasthist': match_pasthist,
        'patient_visits_table':table,
    }
    return render(request, 'patientdata/edit_patient.html', context)


def table_patient(request):
    qs = Patients.objects.all().order_by('-id')

    # search_name = request.GET.get('patname')
    # search_id = request.GET.get('patid')
    # result = Patients.objects.filter(Q(name__icontains=search_name))
    # result_id = Patients.objects.filter(Q(id=search_id))
    
    page_no = request.GET.get('pageno')
    # if search_name != '':
    #     table = PatientsTable(result)
    #     table.paginate(page=request.GET.get("page", 1), per_page=10)
    # elif search_id != None or search_id != '' or int(search_id) != 0:
    #     table = PatientsTable(result_id)
    # elif search_id == None or search_id == '' or int(search_id) == 0:
    #     table = PatientsTable(qs)
    #     table.paginate(page=request.GET.get("page", 1), per_page=10)
    # elif page_no == None or page_no == '' or int(page_no) == 0:
    #     table = PatientsTable(qs)
    #     table.paginate(page=request.GET.get("page", 1), per_page=10)
   
    # elif search_name == '':
    #     table = PatientsTable(qs)
    #     table.paginate(page=request.GET.get("page", 1), per_page=10)
    # elif search_name == '' and  page_no == '' and search_id == '':
    #     table = PatientsTable(result)
    #     table.paginate(page=request.GET.get("page", 1), per_page=2)
    if page_no == None or page_no == '' or int(page_no) == 0:
        table = PatientsTable(qs)
        table.paginate(page=request.GET.get("page", 1), per_page=10)
    elif page_no != None or page_no != '' or int(page_no) != 0:
        table = PatientsTable(qs)
        table.paginate(page=request.GET.get("page", 1), per_page=page_no)
    else:
        table = PatientsTable(qs)
        table.paginate(page=request.GET.get("page", 1), per_page=10) 
    
    context = {
        'table_patient': table
    }
    return render(request, 'patientdata/tables.html', context)


def patient_details(request, barcode):
    qs = Patients.objects.get(barcode=barcode)
    patient = Patients.objects.get(id=qs.id)
    
    context = {
        'qs': qs,
    }
    return render(request, 'patientdata/patient_details.html', context)


def barcode_redirect(request, barcode):
    qs = Patients.objects.get(barcode=barcode)
    
    
    return redirect(reverse('patientdata:edit_patient', args=(qs.id)))





