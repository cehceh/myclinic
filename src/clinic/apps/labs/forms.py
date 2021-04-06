from django import forms
# from django.forms import ModelForm
from .models import LabVisit, LabFollowup
from django.utils.timezone import now
from datetime import date
# from .tables import MedicineTable
from apps.patientdata.models import Patients
from apps.visits.models import Visits

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _



class LabVisitForm(forms.ModelForm):
    name = forms.CharField(error_messages={'required':"This is required, Please fill this field ..."},
                            label='Analysis Name',
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    'id': 'name',
                                #    'lang': 'arabic',
                                    # 'placeholder':'Type Your Drug ...',
                            }))

    result = forms.CharField(required=False, 
                            label='Result',
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    # 'placeholder':'Type Your Plan ...',
                            }))

    resdate = forms.DateField(required=False,
                            label='Result Date',
                            widget=forms.TextInput(
                                attrs={
                                   'class': 'form-control',
                                #    'id': '',
                                #    'lang': 'arabisk',
                                #    'placeholder': 'Type Your Plan ...',
                                # 'readonly':
                               }))
    
    class Meta:
        model = LabVisit
        fields = ('name', 'result', 'resdate', )



class LabFollowupForm(forms.ModelForm):
    name = forms.CharField(error_messages={'required':"This is required, Please fill this field ..."},
                            label='Analysis Name',
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    'id': 'name',
                                #    'lang': 'arabic',
                                    # 'placeholder':'Type Your Drug ...',
                            }))

    result = forms.CharField(required=False, 
                            label='Result',
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    # 'placeholder':'Type Your Plan ...',
                            }))

    resdate = forms.DateField(required=False,
                            label='Result Date',
                            widget=forms.TextInput(
                                attrs={
                                   'class': 'form-control',
                                #    'id': '',
                                #    'lang': 'arabisk',
                                #    'placeholder': 'Type Your Plan ...',
                                # 'readonly':
                               }))
    
    class Meta:
        model = LabFollowup
        fields = ('name', 'result', 'resdate', )
