from django import forms
from .models import Appointment
from apps.patientdata.models import Patients
from django.utils.timezone import now
from datetime import date
from django.db.models import Sum, Max, Count
# from myproject.tables.table_clinic import MedicineTable

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# from django.contrib.postgres.search import SearchVector

class AppointmentForm(forms.ModelForm):
    id = forms.IntegerField(label='Booking ID', required=False,
                           widget=forms.NumberInput(
                               attrs={
                                   'class': 'form-control',
                                   'readonly': 'readonly',
                                #    'value':'',
                                #    'style':'background-color: lightgreen',
                               })
                           )

    patient = forms.ModelChoiceField(queryset=Patients.objects.all(), to_field_name='name', 
    # patient = forms.CharField(required=True, label='Patient Name',
                            # widget=forms.TextInput(
                            widget=forms.Select(
                                attrs={
                                   'class': 'form-control',
                                    #    'id': '',
                                    # 'type':'text',
                                    # 'disabled':'disabled'
                               }
                           ))

    bookdate = forms.DateField(required=True, label='Date',
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    'id': 'bookdate',
                                    'type':'text',
                                    'value':date.today(),
                                    # 'placeholder':date.today(),


                               })
                            )
    starttime = forms.CharField(required=True, label='Time From',
                           widget=forms.TextInput(
                               attrs={
                                    'class': 'form-control',
                                    'placeholder':'Write time of start booking...',
                                #    'id': '',
                                    'type':'number',

                               })
                            )
    endtime = forms.CharField(required=False, label='Time To',
                           widget=forms.TextInput(
                               attrs={
                                    'class': 'form-control',
                                    'placeholder':'Write time of end booking...',
                                    # 'value': date.today(),
                                    # 'id': 'visitdate',
                                    'type':'number',
                                    # 'readonly': 'readonly'
                               }
                           ))
    booknum = forms.IntegerField(required=True, label='Booking No',
                            widget=forms.NumberInput(
                                attrs={
                                   'class': 'form-control',
                                #    'id': '',
                                    'placeholder':'Write the booking number ...',
                                    'type': 'number',
                                    
                               })
                            )

    def clean(self):
        cleaned_data = super().clean()
        tableid = cleaned_data.get('id')
        name = cleaned_data.get('patient')
        booknum  = cleaned_data.get('booknum')
        bookdate = cleaned_data.get('bookdate')
        starttime = cleaned_data.get('starttime')

        match_id = Appointment.objects.filter(id=tableid).exists()
        match_name = Appointment.objects.filter(patient=name, bookdate=bookdate).exists()
        match_num = Appointment.objects.filter(booknum=booknum, bookdate=bookdate).exists()
        match_start = Appointment.objects.filter(starttime=starttime,  bookdate=bookdate).exists()
        
        name_count = Appointment.objects.filter(patient=name, bookdate=bookdate).count()
        num_count = Appointment.objects.filter(booknum=booknum, bookdate=bookdate).count()
        start_count = Appointment.objects.filter(starttime=starttime, bookdate=bookdate).count()
        lastbooknum = Appointment.objects.values('booknum').filter(bookdate=bookdate).last()
        # lastnum = int(lastbooknum['booknum']) + 1 #(Appointment.objects.latest('booknum')) + 1
        
        qs_last = Appointment.objects.values_list('booknum', flat=True).order_by('-booknum').distinct()
        top_num = Appointment.objects.order_by('-booknum').filter(booknum__in=qs_last)
        
        top_booknum = Appointment.objects.filter(bookdate=bookdate).aggregate(Max('booknum'))
        booknum_top = top_booknum['booknum__max']
        if booknum_top != None:
            booknum_top = top_booknum['booknum__max'] + 1
        else:
            booknum_top = 0
            
        # Getting duplicate files
        dup_name = Appointment.objects.values('patient') \
                                    .annotate(ncount=Count('patient'))\
                                    .filter(patient=name, bookdate=bookdate, ncount__gt=1)

        # duplicate_name = Appointment.objects.filter(patient__in=[item['patient'] for item in dup_name])
        #dup_name['patient']
        records = Appointment.objects.filter(bookdate=bookdate,
                                            patient__in=[item['patient'] for item in dup_name])

        rec = [item.patient for item in records]
        reco = any(rec.count(element) > 1 for element in rec)
        dup_key = []
        for dups in dup_name:
            dup_key.append(dups['patient'])
        
        print('dup_key= ' + str(dup_key), 'dupname_form= ' + str(dup_name), 'records= '+str(records))
        print('reco_form= ' + str(reco), 'rec_form= '+ str(rec), lastbooknum, 'qslast= '+ str(qs_last), 'topnum= ' + str(top_num),top_booknum)
        # s = (dup_key.append(dups['patient']) for dups in dup_name)
        # print ('dup key' + str(dup_key))#((dup_key.append(dups['patient']) for dups in dup_name))#(dup_name)
        # print('dup_name= ' + str(dup_name) + 'name_count= ' + str(name_count))
        # if match_id: # for updating
        
        # if reco:
        # if name_count > 1: #dup_key[0] > 1:
        #     print('name_count= ' + str(name_count))
            # self.add_error('patient', 'not a valid name')
            # raise ValidationError('Patient name already has a book number in this date == ' + str(reco))
        #     # else:
        #     #     self.add_error('patient', 'not a valid name')
        #     #     raise ValidationError('Patient name already has a book number in this date == '+str(name_count))
        # else: # for saving
        #     if not match_id:
        #         if match_name:
        #             self.add_error('patient', 'not a valid name')
        #             raise ValidationError('Patient name already has a book number in this date choose another patient')

        # dup_num = Appointment.objects.values('booknum') \
        #                             .annotate(records=Count('booknum'))\
        #                             .filter(records__gt=1)

        # if reco: # for edit form when update patient
        #     raise ValidationError('Update Patient to a right name, Patient name already has a book number !')


        if not match_id: # If true this means that we are in the saving form
            if match_name: # for saving form
                # self.add_error('patient', 'not a valid name')
                raise ValidationError('Patient name already has a book number in this date choose another patient')

        # if match_num:
        #     if match_num:
        #         pass
        # else:
        if not match_id: # we are in the saving form
            if match_num:
                # self.add_error('booknum', 'not a valid book number')
                raise ValidationError('Book number already taken by another patient it must be ' + str(booknum_top))
        
        # dup_start = Appointment.objects.values('starttime') \
        #                             .annotate(records=Count('starttime'))\
        #                             .filter(records__gt=1)

        if not match_id: # we are in the saving form
            if match_start:
                # self.add_error('starttime', 'Already taken before change book time')
                raise ValidationError('This booking time already exsits for another patient')
        
        return cleaned_data

    class Meta:
        model = Appointment
        fields = ('__all__')