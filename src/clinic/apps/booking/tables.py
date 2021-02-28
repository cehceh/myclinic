import django_tables2 as tables
# from clinic.models import Patients, Visits, Medicine
from .models import Appointment
from datetime import date, datetime
from django.core.exceptions import ValidationError


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

class AppointmentTable(tables.Table):
    booknum = tables.TemplateColumn(
        '<a href="{% url \'booking:edit_book\' record.id %}">{{record.booknum}}</a>',
        verbose_name=u'Booking No') 

    pat = tables.TemplateColumn(
        '<a href="{% url \'booking:edit_book\' record.id %}">{{record.patient}}</a>',
        verbose_name=u'Patient Name')

    bookdate = tables.TemplateColumn(
        '<a href="{% url \'booking:edit_book\' record.id %}">{{record.bookdate}}</a>',
        verbose_name=u'Booking Date')

    start = tables.TemplateColumn(
        '<a href="{% url \'booking:edit_book\' record.id %}">{{record.starttime}}</a>',
        verbose_name=u'Booking Time')

    end = tables.TemplateColumn(
        '<a href="{% url \'booking:edit_book\' record.id %}">{{record.endtime}}</a>'                                                      ,
        verbose_name=u'End Time')

    # dy = datetime.strptime(str(bookdate), '%Y-%m-%d')
    # day = dy.day
    # month = dy.month
    # year = dy.year
    delete = tables.TemplateColumn(
        '<a class="btn btn-outline-danger" href="{% url \'booking:delete_item\' record.id record.bookdate.year record.bookdate.month record.bookdate.day %}" '
        'onclick="return confirm(\'Are you sure you want to delete this Booking Date ?\')">Delete</a>',
        verbose_name='Delete This Book',)

    # def countrow(self, table):
    #     return len(table.rows)
    # def year(self):
    #     dy = datetime.strptime(str(bookdate.today()), '%Y-%m-%d')
    #     day = dy.day
    #     month = dy.month
    #     year = dy.year
    
    class Meta:
        model = Appointment
        template_name = 'django_tables2/bootstrap4.html'
        attrs = {"id": "booking-table"}
        fields = ('booknum', 'pat', 'bookdate', 'start', 'end', 'delete')

   

