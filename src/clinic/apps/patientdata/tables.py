import django_tables2 as tables
from apps.patientdata.models import Patients
# from patientdata.models import PresentHistory
# from django.core.exceptions import ValidationError


def render_footer(bound_column, table):
    # for row in table.data:
    #     s = sum(bound_column.accessor.resolve(row))
    return sum(bound_column.accessor.resolve(row) for row in table.data)
    # s = sum(bound_column.accessor.resolve(row) for row in table.data)
    # return s


def countrow(table):
    return len(table.rows)


# class BillsColumn(tables.Column):
#     column_total = 0
#     def render(self, record):
#         bills = record.certificatebills.all()
#         total_bill = 0
#         for bill in bills:
#             total_bill += bill.bill_amount
#         # accumulate
#         self.column_total += total_bill
#         return round(total_bill, 2)

#     def render_footer(self, bound_column, table):
#         return sum(bound_column.accessor.resolve(row) for row in table.data)


class PatientsTable(tables.Table):
    idno = tables.TemplateColumn(
        '<a href="{% url \'patientdata:edit_patient\' record.id %}">{{ record.id }}</a>',
        verbose_name=u'Patient ID')
    patient = tables.TemplateColumn(
        '<a href="{% url \'patientdata:edit_patient\' record.id %}">{{ record.name }}</a>',
        verbose_name=u'Patient Name')
    tele = tables.TemplateColumn(
        '<a href="{% url \'patientdata:edit_patient\' record.id %}">{{ record.phone }}</a>',
        verbose_name=u'Patient Phone')
    mob = tables.TemplateColumn(
        '<a href="{% url \'patientdata:edit_patient\' record.id %}">{{ record.mobile }}</a>',
        verbose_name=u'Patient Mobile')

    # birth = tables.TemplateColumn(
    #     '<a href="/clinic/edit/patient/{{record.id}}/">{{ record.birth_date }}</a>',
    #     verbose_name=u'Birth Date')
    addr = tables.TemplateColumn(
        '<a href="{% url \'patientdata:edit_patient\' record.id %}">{{ record.address }}</a>',
        verbose_name=u'Address')
    # age = tables.TemplateColumn(
    #     '<a href="/clinic/edit/patient/{{record.id}}/">{{ record.age }}</a>',
    #     verbose_name=u'Age')
    crdid = tables.TemplateColumn(
        '<a href="{% url \'patientdata:edit_patient\' record.id %}">{{ record.cardid }}</a>',
        verbose_name=u'Card_ID')
    followup = tables.TemplateColumn(
        '<a class="btn btn-outline-dark" href="{% url \'gyno:add_gyno\' record.id %}">Add Follow Up</a>',
        verbose_name=u'Follow Up')
    addvis = tables.TemplateColumn(
        '<a class="btn btn-outline-dark" href="{% url \'visits:pass_patient_id\' record.id %}">Add New Visit</a>',
        verbose_name=u'New Visit')
    addpast = tables.TemplateColumn(
        '<a class="btn btn-outline-dark" href="/data/create/past/history/patient/{{record.id}}/">Add Past History</a>',
        verbose_name=u'Past History')

    class Meta:
        model = Patients
        template_name = 'django_tables2/bootstrap4.html'
        attrs = {"id": "patients-table"}
        fields = (
            'idno',
            'patient',
            # 'birth',
            # 'age',
            'tele',
            'mob',
            'addr',
            # 'followup',
            'crdid',
            'addpast',
        )

####################
# def check_column():
#     match_presenthist = PresentHistory.objects.filter(patient={{VisitsTable.record.patient_id}}, visit=VisitsTable.record.id).exists()
#     if match_presenthist:
#         history = tables.TemplateColumn(
#                     '<a class="btn btn-outline-primary" href="/data/present/history/patient/{{record.patient_id}}/visit/{{record.id}}/">Add Present History</a>',
#                     verbose_name=u'Add Present History', visible=False)
#     return history

