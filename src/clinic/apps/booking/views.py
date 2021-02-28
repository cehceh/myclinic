from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from datetime import datetime, date

from django.contrib import messages
from .forms import AppointmentForm
from .models import Appointment
from .tables import AppointmentTable
from apps.patientdata.models import Patients
from django.db.models import Sum, Max, Count

# Create your views here.

def save_book(request):
    # patient = Patients.objects.get(id=patient_id)
    pat_search = request.GET.get('pat')
    if pat_search == None:
        bound_form = AppointmentForm(data={'patient':''})
        # return redirect('booking:save_book')
    elif pat_search != '':
        # result = Patients.objects.filter(Q(name=pat_search))
        name = Patients.objects.values('name').filter(name__icontains=pat_search).first()
        # patid = Patients.objects.values('id').filter(name__icontains=pat_search).first()
        pname = name['name']
        # patient = patid['id']
        # pat_id = Patients.objects.get(id=patient)
        # print(pat_id)
        bound_form = AppointmentForm(data={'patient':pname})
    else:
        bound_form = AppointmentForm(data={'patient':''})
    
    if request.method == 'POST':
        form = AppointmentForm(request.POST or None)
        if form.is_valid():
            bookdt = request.POST.get('bookdate')

            dy = datetime.strptime(bookdt, '%Y-%m-%d')
            day = dy.day
            month = dy.month
            year = dy.year
            # lastbooknum = Appointment.objects.filter(bookdate=bkdt).latest('booknum').booknum
            # param = bookdt.replace('-', '')
            form.save()
            # print('after saving: ' + str(request.POST.get('patient')) + str(day) + str(month) + str(year))
            return redirect(reverse('booking:date_table', args=(year, month, day)))
    else:
        form = AppointmentForm()

    context = {
                'booking_form': form,
                'bound_form': bound_form,
                # 'last': lastbooknum,
                # 'year': year,
                # 'month': month,
                # 'day': day,
            }
    return render(request, 'booking/forms.html', context)


def edit_book(request, id):
    qs = Appointment.objects.get(id=id)
    appid = Appointment.objects.values('id').filter(id=id).first()
    app_id= appid['id']
    print(app_id)
    var = Appointment.objects.values('patient').filter(id=id).first()
    patient = var['patient']
    pname = Patients.objects.get(id=patient)
    
    bookdate = request.POST.get('bookdate')
    bnum = Appointment.objects.values('booknum').filter(id=id).first()
    book_num = bnum['booknum']
    
    bound_form = AppointmentForm(data={'patient':pname})# here we need to put name instead of patient_id look at forms.py 
    form = AppointmentForm(request.POST or None, instance=qs)
    if form.is_valid():
        bookdt = request.POST.get('bookdate')

        dy = datetime.strptime(bookdt, '%Y-%m-%d')
        day = dy.day
        month = dy.month
        year = dy.year
        appoint_id = request.POST.get('id')
        name = request.POST.get('patient')
        num = request.POST.get('booknum')
        pat = Patients.objects.values('id').filter(name=name).first()
        pat_id = pat['id']
        
        form.save()
        dup_name = Appointment.objects\
                                .values('patient')\
                                .annotate(ncount=Count('patient'))\
                                .filter(bookdate=bookdt, ncount__gt=1)
        records = Appointment.objects.filter(bookdate=bookdt, 
                                            patient__in=[item['patient'] for item in dup_name])
        print('rec_edit = '+ str(records) + str(name))#(dup_name, records)
        rec = [item.patient for item in records]
        reco = any(rec.count(element) > 1 for element in rec)
        print('patname= '+str(pat_id), 'rec_edit= '+str(rec), 'dupname_edit= ' +str(dup_name),reco)
        
        dup_num = Appointment.objects\
                                .values('booknum')\
                                .annotate(bcount=Count('booknum'))\
                                .filter(bookdate=bookdt, bcount__gt=1)
        records_num = Appointment.objects.filter(bookdate=bookdt, 
                                            booknum__in=[item['booknum'] for item in dup_num])
        print('recnum_edit = '+ str(records_num) + str(num))#(dup_name, records)
        rec_num = [item.booknum for item in records_num]
        reco_num = any(rec_num.count(element) > 1 for element in rec_num)
        print(rec_num, 'reco_num= ' + str(reco_num))
        top_booknum = Appointment.objects.filter(bookdate=bookdt).aggregate(Max('booknum'))
        booknum_top = top_booknum['booknum__max'] + 1
        if reco:
            messages.success(request, str(name)+ ' is already exists and has a booking No.!')
            return redirect(reverse('booking:edit_book', kwargs={'id': app_id}))
        elif reco_num:
            messages.success(request, 'Booking number ('+str(num)+ ') is already exists !, It must be ('+ str(booknum_top)+')')
            return redirect(reverse('booking:edit_book', kwargs={'id':appoint_id}))
        else:
            return redirect(reverse('booking:date_table', args=(year, month, day)))
            
    context = {
            'edit_booking_form': form,
            'bound_form': bound_form,
            'qs': qs,
    }
    return render(request, 'booking/forms.html', context)


def table_book(request):

    search_date = request.GET.get('d')
    search_patient = request.GET.get('p')
    search_patdate = request.GET.get('pd')
    page_no = request.GET.get('pageno')
    if request.GET.get('pageno') == "0":
        page_no = "1"

    if search_date == "":
        searchtable = AppointmentTable(Appointment.objects.filter(bookdate__startswith=date.today()).order_by('-bookdate'))
        searchtable.paginate(page=request.GET.get('page',1), per_page=page_no)
    elif search_date != '':
        qs = Appointment.objects.filter(bookdate=search_date).order_by('booknum')
        searchtable = AppointmentTable(qs)
        searchtable.paginate(page=request.GET.get('page',1), per_page=page_no)
    else:
        searchtable = AppointmentTable(Appointment.objects.filter(bookdate=date.today()).order_by('-bookdate'))
        searchtable.paginate(page=request.GET.get('page',1), per_page=page_no)


    if search_patient == None and search_patdate == None:
        table = AppointmentTable(Appointment.objects.filter(bookdate=date.today()).order_by('-bookdate'))
        table.paginate(page=request.GET.get('page',1), per_page=25)
    elif search_patient != '' and search_patdate == None and search_date == None:
        qs = Appointment.objects.filter(patient__name__icontains=search_patient).order_by('-id')
        table = AppointmentTable(qs)
        table.paginate(page=request.GET.get('page',1), per_page=25)
    elif search_patient != '' and search_patdate != '':
        qs = Appointment.objects.filter(patient__name__icontains=search_patient, bookdate=search_patdate).order_by('-id')
        table = AppointmentTable(qs)
        table.paginate(page=request.GET.get('page',1), per_page=25)
    elif search_patient != '' and search_date == None:
        qs = Appointment.objects.filter(patient__name__icontains=search_patient).order_by('-id')
        table = AppointmentTable(qs)
        table.paginate(page=request.GET.get('page',1), per_page=25)   
    elif search_patient == None:
        table = AppointmentTable(Appointment.objects.filter(bookdate__startswith=date.today()).order_by('-bookdate'))
        table.paginate(page=request.GET.get('page',1), per_page=25)
    elif search_patdate == None:
        table = AppointmentTable(Appointment.objects.filter(bookdate__startswith=date.today()).order_by('-bookdate'))
        table.paginate(page=request.GET.get('page',1), per_page=25)
    elif search_patient == None and search_patdate != '':
        table = AppointmentTable(Appointment.objects.filter(bookdate__startswith=date.today()).order_by('-bookdate'))
        table.paginate(page=request.GET.get('page',1), per_page=25)
    else:
        table = AppointmentTable(Appointment.objects.filter(bookdate__startswith=date.today()).order_by('-bookdate'))
        table.paginate(page=request.GET.get('page',1), per_page=25)

    # if search_date == None:
    #     dy = "00-00-00"
    # else:
    #     dy = datetime.strptime(search_date, '%Y-%m-%d')
    #     day = dy.day
    #     month = dy.month
    #     year = dy.year
    
    context={
        'book_table': table,
        'search_table': searchtable,
        'sdate': search_date,
        'spat': search_patient,
        'pdate': search_patdate,
        # 'year': year,
        # 'month': month,
        # 'day': day,
    }
    return render(request, 'booking/tables.html', context)


def date_table(request, year, month, day):
    qs = Appointment.objects.filter(bookdate__year=year, bookdate__month=month, bookdate__day=day).order_by('booknum')
    page_no = request.GET.get('pageno')
    if page_no == '':
        table = AppointmentTable(qs)
        table.paginate(page=request.GET.get('page',1), per_page=5)
    elif page_no == None or int(page_no) == 0:
        page_no = '3'
        table = AppointmentTable(qs)
        table.paginate(page=request.GET.get('page',1), per_page=page_no)
    else:
        table = AppointmentTable(qs)
        table.paginate(page=request.GET.get('page',1), per_page=page_no)
    
    # table = AppointmentTable(qs)
    # table.paginate(page=request.GET.get('page',1), per_page=25)
    
    context={
        'book_date_table': table,
        'qs': qs,
        'year': year,
        'month': month,
        'day': day,
        'msg': 'Error',
    }
    return render(request, 'booking/tables.html', context)

def current_date_table(request):
    dy = datetime.strptime(str(date.today()), '%Y-%m-%d')
    cday = dy.day
    cmonth = dy.month
    cyear = dy.year
    
    qs = Appointment.objects.filter(bookdate__year=cyear, bookdate__month=cmonth, bookdate__day=cday).order_by('booknum')
    page_no = request.GET.get('pageno')
    if page_no == '':
        table = AppointmentTable(qs)
        table.paginate(page=request.GET.get('page',1), per_page=2)
    elif page_no == None or int(page_no) == 0:
        page_no = '10'
        table = AppointmentTable(qs)
        table.paginate(page=request.GET.get('page',1), per_page=page_no)
    else:
        table = AppointmentTable(qs)
        table.paginate(page=request.GET.get('page',1), per_page=page_no)
    
    # table = AppointmentTable(qs)
    # table.paginate(page=request.GET.get('page',1), per_page=page_no) 
    
    context = {
        'current_date_table': table,
        'page_no':page_no,
        'cyear': cyear,
        'cmonth': cmonth,
        'cday': cday,
    }
    return render(request, 'booking/tables.html', context)


def delete_item(request, id, year, month, day):
    book = Appointment.objects.get(id=id)
    book.delete()

    return redirect(reverse("booking:date_table", args=(year, month, day)))
