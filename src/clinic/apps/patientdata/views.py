from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.db.models import Sum, Max, Count
from django.db import connection, transaction
from django.contrib import messages
from datetime import date
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
        form = PatientsForm(request.POST or None)
        if form.is_valid():
            name = request.POST.get('name')
            # card = request.POST.get('cardid')
            match = Patients.objects.filter(name=name).exists()
            # match_card = Patients.objects.filter(cardid=card).exists()
            if not match:
                save_form = form.save(commit=False)
                save_form.save()
                pat_id = save_form.id
                Visits.objects.create(patient_id=pat_id, visitdate=date.today(),
                                complain="any comp", sign="any sign", 
                                amount=0, intervention="any intervention")
                #
                # cursor = connection.cursor()
                # cursor.execute('''INSERT INTO clinic_visits(patient_id, visitdate, amount)
                #                 SELECT id, NOW(), 0
                #                 FROM clinic_patients''')
                # # print('done')
                # # cursor.fetchall()
                # transaction.commit
                print('patient: ' + str(name))
                messages.success(request, 'saving done ... ')
                return redirect('patientdata:table_patient')
            else:
                print('what is wrong')
                messages.success(request, 'Patient Name already exsits and can\'t be repeated')
                # return redirect('patientdata:save_patient')
                # raise Http404("try again this name is taken before")
    else:
        form = PatientsForm()

    # lastcardid = int(Patients.objects.latest('id').cardid) + 1

    # label = "_Save_"
    label2 = "Save"
    context = {
        'savepatform': form,
        # 'last': lastcardid,
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

    # patient_id = request.GET['id']#request.POST.get('id')
    # myform = VisitsForm(data={'patient_id':id})  
      
    query = Patients.objects.get(id=id)  # get(birth_date=birth_date)
    patient = Patients.objects.values('id').filter(id=id).first()
    # patient = Patients.objects.filter(id=id)
    patient_id = patient['id']
    # print(query, patient)
    match_pasthist = PastHistory.objects.filter(patient=id).exists()
    # if match_pasthist:
    #     pasthist = PastHistory.objects.values('id').filter(patient=patient_id).first()
    
    form = PatientsForm(request.POST or None, instance=query)
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
        dup_num = Patients.objects\
                            .values('cardid')\
                            .annotate(bcount=Count('cardid'))\
                            .filter(cardid=card, bcount__gt=1)
        records_num = Patients.objects.filter(cardid__in=[item['cardid'] for item in dup_num])
        # print('recnum_edit = '+ str(records_num) + str(num))#(dup_name, records)
        rec_num = [item.cardid for item in records_num]
        reco_num = any(rec_num.count(element) > 1 for element in rec_num)
        # print(rec_num, 'reco_num= ' + str(reco_num))
        # top_booknum = Patients.objects.filter(bookdate=bookdt).aggregate(Max('booknum'))
        # booknum_top = top_booknum['booknum__max'] + 1
        if reco or reco_num:
            # messages.success(request, 'Patient and Card ID must be unique change them ..!')
            # return redirect(reverse('patientdata:edit_patient', kwargs={'id': id}))
            if reco:
                messages.success(request, 'Patient (' +str(name)+ ') is already exists change the name ..!')
                return redirect(reverse('patientdata:edit_patient', kwargs={'id': id}))
            elif reco_num:
                messages.success(request, 'Card ID is already exists !, It must not be duplicated')
                return redirect(reverse('patientdata:edit_patient', kwargs={'id':id}))
        # elif reco:
        #     messages.success(request, 'Patient (' +str(name)+ ') is already exists change the name ..!')
        #     return redirect(reverse('patientdata:edit_patient', kwargs={'id': id}))
        # elif reco_num:
        #     messages.success(request, 'Card ID is already exists !, It must not be duplicated')
        #     return redirect(reverse('patientdata:edit_patient', kwargs={'id':id}))
        else:
            return redirect(reverse('patientdata:table_patient'))
            
        # return redirect('patientdata:table_patient')
        # return redirect(query.get_absolute_url())
    context = { 
        'patient': patient,
        'patient_id': patient_id,
        'editpatform': form,
        'query': query,
        'match_pasthist': match_pasthist,
        'patient_visits_table':table,
    }
    return render(request, 'patientdata/edit_patient.html', context)


def table_patient(request):
    qs = Patients.objects.all().order_by('-id')

    page_no = request.GET.get('pageno')
    if page_no == None or page_no == '' or int(page_no) == 0:
        table = PatientsTable(qs)
        # table = VisitsTable(results, exclude='addrevis, addpresent')
        table.paginate(page=request.GET.get("page", 1), per_page=10)
    else:
        table = PatientsTable(qs)
        # table = VisitsTable(results, exclude='addrevis, addpresent')
        table.paginate(page=request.GET.get("page", 1), per_page=page_no)
    
    # table = PatientsTable(qs)
    # table.paginate(page=request.GET.get("page", 1), per_page=10)
    context = {
        'table_patient': table
    }
    return render(request, 'patientdata/tables.html', context)
  # HttpResponse for http direct write


# def table_visits(requset, id):
#     qs = Visits.objects.filter(id=id).order_by('-id')
#     print(qs)
#     table = PatientsTable(qs)
#     table.paginate(page=request.GET.get("page", 1), per_page=10)
#     context = {
#         'table_patient': table
#     }
#     return render(request, 'tables.html', context)
