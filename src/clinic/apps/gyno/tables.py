import django_tables2 as tables
from apps.patientdata.models import Patients
from apps.gyno.models import Obestetric, Menstrual


def render_footer(bound_column, table):
    return sum(bound_column.accessor.resolve(row) for row in table.data)


def countrow(table):
    return len(table.rows)


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
            'crdid',
            'addpast',
        )