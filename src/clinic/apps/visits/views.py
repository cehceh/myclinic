from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Visits
from apps.patientdata.models import Patients
from apps.presenthistory.models import PresentHistory
from apps.pasthistory.models import PastHistory

from apps.revisits.models import Revisits
from .forms import VisitsForm
from .tables import VisitsTable
from apps.visitdrug.tables import MedicineTable
from apps.visitdrug.models import Medicine
from django.contrib import messages

from django_tables2.config import RequestConfig
from django_tables2.export.export import TableExport


def export_table(request):
    table = VisitsTable(Visits.objects.all())

    RequestConfig(request).configure(table)

    export_format = request.GET.get("csv, json", None)
    if TableExport.is_valid_format(export_format):
        # exclude columns while creating the TableExport instance:
        # exporter = TableExport("csv", table, exclude_columns=("image", "buttons"))
        exporter = TableExport(export_format, table, dataset_kwargs={"title": "My Custom Sheet Name"})
        # exporter = TableExport(export_format, table)
        return exporter.response("table.{}".format(export_format))

    return render(request, "tables.html", {
        "export_table": table,
    })

# old save visit
# def save_visits(request): # save without
#     ''' Method for saving patient's visits '''
#     if request.method == 'POST':
#         form = VisitsForm(request.POST or None)
#         if form.is_valid():
#             # patient_id = form.cleaned_data['patient_id']
#             form.save()
#             return redirect('/clinic/table/visits/')
#     else:
#         form = VisitsForm()
#     context = {
#         'save_visits_form': form,
#     }
#     return render(request, 'clinic/forms.html', context)


# new save visit
def pass_patient_id(request, id): # Making save to new visits
    patient = Patients.objects.get(id=id) # out put is the patient name
    patient_id = Patients.objects.values('id').filter(id=id).first() # This is out put of without .first()=> <QuerySet [{'id': 36}]>
    var = patient_id['id']
    # var1 = Patients.objects.values('mobile').filter(id=id).first()
    # var11 = var1['mobile']
    # print(patient, patient_id)
    match_pasthist = PastHistory.objects.filter(patient=id).exists()

    bound_form = VisitsForm(data={'patient':patient})
    
    if request.method == 'POST':
        form = VisitsForm(request.POST or None)
        if form.is_valid():
            save_form = form.save(commit=False)
            save_form.patient_id = var
            save_form.save()
            visit_id = save_form.id
            # name = save_form.patient
            messages.success(request, 'Saving new visit for (' + str(patient) + ') done')
            return redirect(reverse('visits:visits_patient_id', args=(visit_id, save_form.patient_id)))#('visits:table_visits')
    else:
        form = VisitsForm()
    context = {
        'pat_id': var,
        'patient': patient,
        'match_pasthist':match_pasthist,
        'save_visits_form': form,
        'bound_form': bound_form,
    }
    return render(request, 'visits/add_visit.html', context)


# new edit visit
def visits_patient_id(request, id, patient_id):  # Making Update to a visit with knowing the patient id
    query = Visits.objects.get(id=id)  # out put Visit ID
    qs = Visits.objects.values('id', 'patient_id').filter(id=id, patient_id=patient_id).first() # {'patient_id': 2}
    # for get_url() to redirect to -save present history- form
    visid = Visits.objects.values('id')\
                        .filter(id=id).first()  # {'id': 136, 'patient': 15}
    vis_id = visid['id']
    
    match_medicine = Medicine.objects.filter(visit=id).exists()
    # if match_medicine:
    #     medicine = Medicine.objects.get(visit=id)
    # else:
    #     medicine = None

    match_present = PresentHistory.objects.filter(visit=id).exists()
    # if not match_present:
    #     present = None #PresentHistory.objects.all()
    # else:
    
    present = PresentHistory.objects.values('id').filter(visit=id).first()
    if present != None:
        presentid = present['id']
    else:
        presentid = 0
    # print(present, presentid)
    if presentid == 0:
        present_qs = 0
    else:
        present_qs = PresentHistory.objects.get(id=presentid)

    match_revisit = Revisits.objects.filter(visit=id).exists()
   
    patient = Patients.objects.get(id=patient_id) # Use it with get_absolute_url()
    patientid = qs['patient_id'] # out put is Patient ID
    form = VisitsForm(request.POST or None, instance=query)
    if form.is_valid():
        # patid = request.POST.get('patient')
        # # print('patid : ' + str(patid))
        # match = Visits.objects.filter(patient_id=patid, id=id).exists()
        # if match:
        save_form = form.save(commit=False)
        save_form.patient_id = patient_id
        # save_form.visit_id = id
        save_form.save()
        messages.success(request, 'Update visit no. (' + str(vis_id) + ') done successfully' )
        return redirect(reverse('visits:visits_patient_id', args=(vis_id, patientid)))  # ('/clinic/table/')
        #  HTTPResponseRedirect(reverse('clinic:edit_patient', kwargs={'id': id}))
        # else:
        #     messages.success(request, 'The Patient Name Must Be : ' + \
        #     str(patient) + ', With Patient ID : ' + str(patient_id) + ' Not Ptient ID : ' + str(patid))

    context = {
        # 'saveDone': match,
        'patient': patient,
        'patient_id': patientid,
        'visit': query,
        'vis_id': vis_id,
        'qs': qs,
        'medicine': match_medicine,
        # 'medicine_id': medicine,
        'match_present': match_present,
        'present_id': present_qs,
        'match_revisit': match_revisit,
        # 'revisit': revisit,
        'edit_visits_form': form,
    }
    return render(request, 'visits/edit_visit.html', context)


def table_visits(request):
    qs = Visits.objects.select_related('patient').order_by('-id') # the next lines are the result of this query ORM
    # qs = Medicine.objects.select_related('patient').order_by('-id')
    # ''' SELECT "clinic_visits"."id", "clinic_visits"."patient_id", "clinic_visits"."visitdate",
    # "clinic_visits"."complain", "clinic_visits"."sign", "clinic_visits"."diagnosis", "clinic_visits"."intervention",
    # "clinic_visits"."amount", "clinic_patients"."id", "clinic_patients"."name", "clinic_patients"."address", 
    # "clinic_patients"."birth_date", "clinic_patients"."age", "clinic_patients"."phone", "clinic_patients"."mobile",
    # "clinic_patients"."cardid" FROM "clinic_visits" 
    # LEFT OUTER JOIN "clinic_patients" 
    # ON ("clinic_visits"."patient_id" = "clinic_patients"."id") 
    # ORDER BY "clinic_visits"."id" DESC '''

    # qs = Visits.objects.all().order_by('-id')
    page_no = request.GET.get('pageno')
    if page_no == None or int(page_no) == 0 or page_no == '':
        table = VisitsTable(qs, exclude='addpresent')
        table.paginate(page=request.GET.get("page", 1), per_page=100)
    else:
        table = VisitsTable(qs, exclude='addpresent')
        table.paginate(page=request.GET.get("page", 1), per_page=page_no)

    print(qs.query)
    context = {
        'qs_table': qs,
        'visits_table': table,
    }
    return render(request, 'visits/tables.html', context)
# HttpResponse for http direct write

