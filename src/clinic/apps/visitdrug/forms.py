from django import forms
# from django.forms import ModelForm
from .models import Medicine
from django.utils.timezone import now
from datetime import date
from .tables import MedicineTable
from apps.patientdata.models import Patients
from apps.visits.models import Visits


from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _



class MedicineForm(forms.ModelForm):
    patient = forms.ModelChoiceField(queryset=Patients.objects.all(), required=True, label='Patient Name',
                           widget=forms.Select(
                               attrs={
                                   'class': 'form-control',
                                   'id': 'patient',
                                #    'v-model': "patient_name",
                                    # 'disabled':'disabled'
                               }))

    # visit = forms.CharField(required=True, label='Visit ID No.',
    #                        widget=forms.TextInput(
    #                            attrs={
    #                                 'class': 'form-control',
    #                                 'id': 'visit_id',
    #                                 'readonly':'readonly'
    #                            }))
    visit = forms.ModelChoiceField(queryset=Visits.objects.all(), required=True, label='Visit No.',
                           widget=forms.Select(
                               attrs={
                                   'class': 'form-control',
                                   'id': 'visit-id',
                                    # 'readonly':'readonly'
                               }))

    name = forms.CharField(error_messages={'required':"Please fill this field ..."}, label='Drug',
                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'form-control',
                                       'id': 'name',
                                    #    'lang': 'arabic',
                                        'placeholder':'Type Your Drug ...',
                                   }))

    plan = forms.CharField(required=False, label='Plan',
                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'form-control',
                                       'id': 'plan',
                                       'lang': 'arabisk',
                                        'placeholder':'Type Your Plan ...',
                                   }))

    presc = forms.CharField(required=False,
                           label='Pre ID',
                           widget=forms.TextInput(
                               attrs={
                                   'class': 'form-control',
                                #    'id': '',
                                #    'lang': 'arabisk',
                                #    'placeholder': 'Type Your Plan ...',
                                # 'readonly':
                               }))
    # def clean(self):  # this method for prevent save or update the field 'amount' if it is None
    #     cleaned_data = super().clean()
    #     pat = cleaned_data.get('patient')
    #     vis = cleaned_data.get('visit')
    #     print('visit: ' + str(vis) + ', pat: ' + str(pat))
    #     # drug = cleaned_data.get('name')
    #     # plan = cleaned_data.get('plan')
    #     match_drug = Medicine.objects.filter(visit=vis, patient=pat).exists()
    # match = Visits.objects.filter(id=vis, patient=pat).exists()
    # # row = countrow
    # if match == False:
    #     self.add_error('patient', 'patient is not allowed'
    #                    )  # the error as outline (red line) of the input
    #     self.add_error('visit', 'visit is not allowed'
    #                    )  # the error as outline (red line) of the input
    #     raise ValidationError('Please don\'t change patient name or visit')
    # if not match_drug:
    #     raise ValidationError('Add drugs to this prescription')
    # return cleaned_data

    # def countrow(self, table):
    #     return len(table.rows)

    class Meta:
        model = Medicine
        fields = ('__all__')
        # fields = ('__str__', 'address', )

    # def clean(self):
    #     cleaned = super().clean()
    #     visit_id = cleaned.get('visit')
    #     table = MedicineTable(Medicine.objects.filter(visit=visit_id))
    #     # row_count = self.countrow(MedicineTable)
    #     row_count = len(table.rows)
    #     if row_count > 2:
    #         raise ValidationError('Drugs must be 2 or less')

    # these three lines make the error appears in the templates
    # <div style="background-color: pink;">
    #         {{save_visits_form.non_field_errors}}
    #     </div>
    # return cleaned_data
