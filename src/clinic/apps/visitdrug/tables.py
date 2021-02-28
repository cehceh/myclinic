import django_tables2 as tables
# from clinic.models import Patients, Visits, Medicine
from .models import Medicine


class MedicineTable(tables.Table):
    vit = tables.TemplateColumn(
        '<a href="/clinic/patient/{{record.patient_id}}/visit/{{record.visit}}/drug/{{record.id}}/">\
                                {{ record.visit }}</a>'                                                       ,
        verbose_name=u'Visit ID',
        visible=False)

    pat = tables.TemplateColumn(
        '<a href="/clinic/patient/{{record.patient_id}}/visit/{{record.visit}}/drug/{{record.id}}/">\
                                {{ record.patient }}</a>'                                                         ,
        verbose_name=u'Patient')

    drug = tables.TemplateColumn(
        '<a href="/clinic/patient/{{record.patient_id}}/visit/{{record.visit}}/drug/{{record.id}}/">\
                                {{ record.name }}</a>'                                                      ,
        verbose_name=u'Drug')

    plan = tables.TemplateColumn(
        '<a href="/clinic/patient/{{record.patient_id}}/visit/{{record.visit}}/drug/{{record.id}}/">\
                                {{ record.plan }}</a>'                                                      ,
        verbose_name=u'Plan')
    delete = tables.TemplateColumn(
        '<a class="btn btn-outline-danger" href="/clinic/patient/{{record.patient_id}}/visit/{{record.visit}}/delete/drug/{{record.id}}/" '
        'onclick="return confirm(\'Are you sure you want to delete this Drug ?\')">Delete</a>',
        verbose_name='Delete Drug',
    )

    # def countrow(self, table):
    #     return len(table.rows)

    class Meta:
        model = Medicine
        template_name = 'django_tables2/bootstrap4.html'
        attrs = {"id": "medicine-table"}
        fields = ('pat', 'vit', 'drug', 'plan', 'delete')

    # def clean(self):
    #     row_count = self.countrow(MedicineTable)
    #     if row_count > 2:
    #         raise ValidationError('Drugs must be 2 or less')
    #     return row_count

