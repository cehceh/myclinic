from django import forms
from django.forms import ModelForm
from .models import Patients
from django.utils.timezone import now
from datetime import date
from apps.visitdrug.tables import MedicineTable
from apps.visitdrug.models import Medicine
from apps.visits.models import Visits

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# from django.contrib.postgres.search import SearchVector

def validate_none(value):
    if value == None:
        raise ValidationError(_('%(value)s must be not NONE'),
            params={'value': '0'},
        )

        
# you will write your class forms to be appear to the users
class PatientsForm(forms.ModelForm):
    id = forms.IntegerField(required=False, label='Patient ID',
                           widget=forms.NumberInput(
                               attrs={
                                   'class': 'form-control',
                                   'readonly': 'readonly',
                               })
                           )
    name = forms.CharField(required=True,
            widget=forms.TextInput(
                attrs={
                    'class':'form-control',
                    'id': 'patient-name',
                }
            ))
    address = forms.CharField(required=False,
            widget=forms.TextInput(
                attrs={
                    'class':'form-control',
                    'id': 'address',
                }
            ))
    birth_date = forms.DateField(required=True,
            widget=forms.TextInput(
                attrs={
                    'class':'form-control',
                    'id': 'birth-date',
                    'type': 'text',
                    'name': 'dob',
                    # 'placeholder': date.today(),
                    # 'readonly': 'readonly', # to make an input disabled
                })
            )
    cardid = forms.CharField(required=True,
            widget=forms.TextInput(
                attrs={
                    'class':'form-control',
                    'id': 'cardid',
                    # 'type': 'number',
                }
            ))
    phone = forms.CharField(required=False,
            widget=forms.TextInput(
                attrs={
                    'class':'form-control',
                    'id': 'phone',
                }
            ))
    mobile = forms.CharField(required=False,
            widget=forms.TextInput(
                attrs={
                    'class':'form-control',
                    'id': 'mobile',
                }
            ))
    age = forms.CharField(required=True,
            widget=forms.TextInput(
                attrs={
                    'class':'form-control',
                    'id': 'age',
                    'type': 'number',
                    'name': 'age',
                    # 'readonly': 'readonly', # to make an input disabled
                }
            ))

    def clean(self):
        cleaned_data = super().clean()
        patid = cleaned_data.get('id')
        match_id = Patients.objects.filter(id=patid).exists()
        cardid = cleaned_data.get('cardid')
        match = Patients.objects.filter(cardid=cardid).exists()
        # lastcardid = int(Patients.objects.latest('id').cardid) + 1 #all().order_by('-cardid')[0]
        # print(lastcardid)
        if not match_id:
            if match == True or cardid == None:
                self.add_error('cardid', 'Card ID must not be Empty or Repeated') # the error as outline (red line) of the input
                raise ValidationError('Card ID must not be Empty or Repeated')
        # else:
        #     raise ValidationError('Card ID must not be Empty or Repeated')
        return cleaned_data

    class Meta:
        model = Patients
        fields = ('__all__')
        # fields = ('__str__', 'address', )




# class VisitsForm(forms.ModelForm):
#     # query = Visits.objects.filter(id=id).exists()
#     # def match_id():
#     #     cleaned_data = super().clean()
#     #     vid = cleaned_data.get('id')
#     #     return Visits.objects.filter(id=vid).exists()

#     # print(match_id(id))
#     # id = 0
#     # if match_id:
#     #     id = forms.IntegerField(required=False, label='Visit No.',
#     #                        widget=forms.NumberInput(
#     #                            attrs={
#     #                                'class': 'form-control',
#     #                                'readonly': 'readonly',
#     #                                'style':('background-color', 'lightgreen')
#     #                            })
#     #                        )
#     # else:
#     #     id = forms.IntegerField(required=False, label='Visit No.',
#     #                        widget=forms.NumberInput(
#     #                            attrs={
#     #                                'class': 'form-control',
#     #                                'readonly': 'readonly',
#     #                                'style':{'background-color': 'pink'}
#     #                            })
#     #                        )
#     # print(match_id(id))

#     id = forms.IntegerField(required=False, label='Visit No.',
#                            widget=forms.NumberInput(
#                                attrs={
#                                    'class': 'form-control',
#                                    'readonly': 'readonly',
#                                 #    'style': ('background-color:lightgreen')
#                                })
#                            )
#     patient = forms.ModelChoiceField(queryset=Patients.objects.all(), required=True, label='Name',
#                            widget=forms.Select(
#                                attrs={
#                                    'class': 'form-control',
#                                     'id': 'patient',
#                                     # 'disabled':'disabled'
#                                }
#                            ))

#     complain = forms.CharField(required=False, label='Complain',
#                            widget=forms.Textarea(
#                                attrs={
#                                    'class': 'form-control',
#                                 #    'id': '',

#                                })
#                             )
#     sign = forms.CharField(required=False, label='Sign',
#                            widget=forms.Textarea(
#                                attrs={
#                                    'class': 'form-control',
#                                 #    'id': '',

#                                })
#                             )
#     visitdate = forms.DateField(required=False, label='Visit Date',
#                            widget=forms.TextInput(
#                                attrs={
#                                     'class': 'form-control',
#                                     'placeholder':'Click here to enter the visit date ...',
#                                     'value': date.today(),
#                                     'id': 'visitdate',
#                                     'type':'text',
#                                     # 'readonly': 'readonly'
#                                }
#                            ))
#     diagnosis = forms.CharField(required=False, label='Daignosis',
#                             widget=forms.TextInput(
#                                 attrs={
#                                    'class': 'form-control',
#                                 #    'id': '',

#                                })
#                             )
#     intervention = forms.CharField(required=False, label='Intervention',
#                             widget=forms.TextInput(
#                                 attrs={
#                                    'class': 'form-control',
#                                 #    'id': '',

#                                })
#                             )
#     amount = forms.IntegerField(required=False, label='Amount', #validators=[validate_none],
#                            widget=forms.NumberInput(
#                                attrs={
#                                    'class': 'form-control',
#                                 #    'id': '',
#                                     'value':'0'
#                                }
#                            ))

#     def clean(self): # this method for prevent save or update the field 'amount' if it is None
#         cleaned_data = super().clean()
#         amount = cleaned_data.get('amount')
#         visitdate = cleaned_data.get('visitdate')
#         if amount == None:
#             # self.add_error('amount', 'can not be None') # the error as outline (red line) of the input
#             raise ValidationError('Amount Can Not Be Empty')
#         if visitdate == None:
#             self.add_error('visitdate', 'Date can\'t be Empty')
#             raise ValidationError('Visit Date Can Not Be Empty')
#             # return msg
#         return cleaned_data

#     # def get_id(self):
#     #     cl = super().get_id()
#     #     vid = cl.get('id')
#     #     query = Visits.objects.filter(id=vid).exists()
#     #     return query
#     # print('get = ' + str(get_id.vid))

#     class Meta:
#         model = Visits
#         fields = ('__all__')#('id', 'patient')#('__all__')
#         # fields = ('__str__', 'address', )
        
    # def __init__(self, *args, **kwargs):
    #     super(VisitsForm, self).__init__(*args, **kwargs)
    #     # self.id = self.fields['id']
    #     # self.fields['id'].widget.attrs['class'] = 'input'
        
    #     # cl = super().clean()
    #     # self.fields['id'] = self.clean()
        
    #     # v = get_id
    #     # query = Visits.objects.filter(id=self.id.id).exists()
    #     # if query:
    #     #     self.fields['id'].widget.attrs['style'] = ('background-color:lightgreen')
    #     # else:
    #     #     self.fields['id'].widget.attrs['style'] = ('background-color:lightpink')

    #     # self.fields['patient'].widget.attrs['class'] = 'input'
    #     # print('get = ' + str(get_id))
    #     # f = self.fields['id']
    #     f = True 
    #     # # v_id = super.get('id')
    #     if f:
    #         vid = kwargs['instance']
    #         query = Visits.objects.filter(id=vid.id).exists()
    #     else:
    #         query = False

    #     if query:
    #         self.fields['id'].widget.attrs['style'] = ('background-color:lightgreen')
    #     else:
    #         self.fields['id'].widget.attrs['style'] = ('background-color:lightpink')

    #     self.fields['patient'].widget.attrs['class'] = 'input'
        # print('vidvid = ' + str(vid))
        # print(v_id)
        # self.fields['patient'].widget.attrs['style'] = ('background-color:lightgreen')
        # self.fields['description'].widget.attrs['class'] = 'textarea'



# class MedicineForm(forms.ModelForm):
#     patient = forms.ModelChoiceField(queryset=Patients.objects.all(), required=True, label='Patient Name',
#                            widget=forms.Select(
#                                attrs={
#                                    'class': 'form-control',
#                                    'id': 'patient',
#                                 #    'v-model': "patient_name",
#                                     # 'disabled':'disabled'
#                                }))

#     # visit = forms.CharField(required=True, label='Visit ID No.',
#     #                        widget=forms.TextInput(
#     #                            attrs={
#     #                                 'class': 'form-control',
#     #                                 'id': 'visit_id',
#     #                                 'readonly':'readonly'
#     #                            }))
#     visit = forms.ModelChoiceField(queryset=Visits.objects.all(), required=True, label='Visit No.',
#                            widget=forms.Select(
#                                attrs={
#                                    'class': 'form-control',
#                                    'id': 'visit-id',
#                                     # 'readonly':'readonly'
#                                }))

#     name = forms.CharField(error_messages={'required':"Please fill this field ..."}, label='Drug',
#                                widget=forms.TextInput(
#                                    attrs={
#                                        'class': 'form-control',
#                                        'id': 'name',
#                                     #    'lang': 'arabic',
#                                         'placeholder':'Type Your Drug ...',
#                                    }))

#     plan = forms.CharField(required=False, label='Plan',
#                                widget=forms.TextInput(
#                                    attrs={
#                                        'class': 'form-control',
#                                        'id': 'plan',
#                                        'lang': 'arabisk',
#                                         'placeholder':'Type Your Plan ...',
#                                    }))

#     presc = forms.CharField(required=False,
#                            label='Pre ID',
#                            widget=forms.TextInput(
#                                attrs={
#                                    'class': 'form-control',
#                                 #    'id': '',
#                                 #    'lang': 'arabisk',
#                                 #    'placeholder': 'Type Your Plan ...',
#                                 # 'readonly':
#                                }))
#     # def clean(self):  # this method for prevent save or update the field 'amount' if it is None
#     #     cleaned_data = super().clean()
#     #     pat = cleaned_data.get('patient')
#     #     vis = cleaned_data.get('visit')
#     #     print('visit: ' + str(vis) + ', pat: ' + str(pat))
#     #     # drug = cleaned_data.get('name')
#     #     # plan = cleaned_data.get('plan')
#     #     match_drug = Medicine.objects.filter(visit=vis, patient=pat).exists()
#     # match = Visits.objects.filter(id=vis, patient=pat).exists()
#     # # row = countrow
#     # if match == False:
#     #     self.add_error('patient', 'patient is not allowed'
#     #                    )  # the error as outline (red line) of the input
#     #     self.add_error('visit', 'visit is not allowed'
#     #                    )  # the error as outline (red line) of the input
#     #     raise ValidationError('Please don\'t change patient name or visit')
#     # if not match_drug:
#     #     raise ValidationError('Add drugs to this prescription')
#     # return cleaned_data

#     # def countrow(self, table):
#     #     return len(table.rows)

#     class Meta:
#         model = Medicine
#         fields = ('__all__')
#         # fields = ('__str__', 'address', )

#     # def clean(self):
#     #     cleaned = super().clean()
#     #     visit_id = cleaned.get('visit')
#     #     table = MedicineTable(Medicine.objects.filter(visit=visit_id))
#     #     # row_count = self.countrow(MedicineTable)
#     #     row_count = len(table.rows)
#     #     if row_count > 2:
#     #         raise ValidationError('Drugs must be 2 or less')

#     # these three lines make the error appears in the templates
#     # <div style="background-color: pink;">
#     #         {{save_visits_form.non_field_errors}}
#     #     </div>
#     # return cleaned_data
