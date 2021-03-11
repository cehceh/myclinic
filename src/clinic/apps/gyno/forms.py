from django import forms
from datetime import date
from django.forms import inlineformset_factory
from .models import (Obestetric, Menstrual, MedHistory,
                    SurHistory, GynHistory, DrugHistory)



## Make DateInput
# class DateInput(forms.DateInput):
#     input_type = 'date'



class ObestetricForm(forms.ModelForm):
    # GYNA = (
    #     (True, 'Not Pregnant'),
    #     (False, 'Pregnant'),
    # )
    class Meta:
        model = Obestetric
        fields = ('patient','obdate','gyn','g','p','a','nvd','cs','ld','lc','hist')
        GYNA = (
            (True, 'Not Pregnant'),
            (False, 'Pregnant'),)
        widgets = {
            'patient': forms.Select(
                attrs={
                    'class': 'form-control',
                    # 'type': "date",
                    }),
            'obdate': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': "date",
                    'value': date.today(),
                    }),
            'gyn': forms.Select(
                choices=GYNA,
                attrs={
                    'class': 'form-control',
                }
            ),
            'g': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'readonly': 'readonly',
                }),
            'p': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                }),
            'a': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                }),
            'nvd':forms.CheckboxInput(
                attrs={
                    'class': 'form-control',
                    "name":"rad",
                    "color":"primary",
                }),
            'cs':forms.CheckboxInput(
                attrs={
                    'class': 'form-control',
                    "name":"rad",
                    "color":"danger",
                }),
            'ld':forms.TextInput(
                attrs={
                    'class': 'form-control',
                }),
            'lc':forms.TextInput(
                attrs={
                    'class': 'form-control',
                }),
            'hist':forms.Textarea(
                attrs={
                    'class': 'form-control',
                }),                
        }


class MenstrualForm(forms.ModelForm):
    # lmp = forms.DateField(
    #     widget=forms.DateInput(
    #     attrs={
    #         'type': 'date',
    #     }
    # ))
    class Meta:
        model = Menstrual
        fields = ('lmp', 'edd', 'ga', 'remain',)
        widgets = {
            'lmp': forms.DateInput( 
                # format=['%Y-%m-%d'],
                attrs={
                    'class': 'form-control',
                    'type':'date',
                    # 'format':'yy-MM-dd',
                    'value': date.today(),
                }),
            'edd': forms.DateInput( 
                attrs={
                    'class': 'form-control',
                    'type':'date',
                }),
            'ga': forms.TextInput( 
                attrs={
                    'class': 'form-control',
                    'type':'text',
                }),
            'remain': forms.TextInput( 
                attrs={
                    'class': 'form-control',
                    'type':'text',
                }),
        }

        # exclude = ('obestetric', 'patient',)


class MedHistoryForm(forms.ModelForm):
    
    class Meta:
        model = MedHistory
        fields = ('name',)
        # fields = ('__all__')
        # exclude = ('obestetric', 'patient',)


class SurHistoryForm(forms.ModelForm):
    
    class Meta:
        model = SurHistory
        fields = ('name',)
        # fields = ('__all__')
        # exclude = ('obestetric', 'patient',)


class GynHistoryForm(forms.ModelForm):
    
    class Meta:
        model = GynHistory
        fields = ('name',)
        # fields = ('__all__')
        # exclude = ('obestetric', 'patient',)


class DrugHistoryForm(forms.ModelForm):
    
    class Meta:
        model = DrugHistory
        fields = ('name',)
        # fields = ('__all__')
        # exclude = ('obestetric', 'patient',)



