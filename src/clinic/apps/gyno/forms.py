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
            (False, 'Pregnant'),
        )
        widgets = {
            'obdate': forms.DateInput(
                attrs={
                    'type': "date",
                    'value': date.today(),
                    }),
            'gyn': forms.Select(
                choices=GYNA,
            ),
            'g': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'readonly': 'readonly',
                }),
            'p': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    # 'readonly': 'readonly',
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
                    'type':'date',
                    # 'format':'yy-MM-dd',
                    'value': date.today(),
                }),
            'edd': forms.DateInput( 
                # format=['%Y-%m-%d'],
                attrs={
                    'type':'date',
                    # 'value': date.today(),
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



