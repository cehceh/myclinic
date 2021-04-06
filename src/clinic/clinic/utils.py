from django.core.exceptions import PermissionDenied

# from django.core.exceptions import 
from django.contrib import messages
import os, re, uuid, datetime, random, string
from django.http import HttpResponse
from typing import ContextManager
from django.template.loader import get_template

from django.utils import timezone
from django.utils.text import slugify
# from bidi import algorithm as bidialg
from io import BytesIO
from xhtml2pdf import pisa

# from simple_decorators.apps.models import Entry


# Decorator for check mac address
def auth_required(function):
    def wrap(request, *args, **kwargs):
        # joins elements of getnode() after each 2 digits. 
        # using regex expression 
        label = os.environ.get('SERIAL')
        # print (label) 
        mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
        # print (mac) 
        if mac == label:
            # messages.success(request, 'you are authorized')
            return function(request, *args, **kwargs)
        else:
            # messages.success(request, 'you are not authorized')
            raise PermissionDenied

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


# 
def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()

    ''' important notes about rendring html to pdf via 'pisa' next three lines are working good to fix the problem
    of Arabic language except the letters are separated 
    '''
    # pdf = pisa.CreatePDF(bidialg.get_display(html, base_dir="L"), result, encoding='iso-8859-6') # CreatePDF = pisaDocument
    # pdf = pisa.pisaDocument(BytesIO(bidialg.get_display(html.encode('utf-8'), base_dir='L')), result)
    # pdf = pisa.pisaDocument(bidialg.get_display(html.encode('UTF-8')), result)
    
    pdf = pisa.CreatePDF(BytesIO(html.encode("UTF-8")), result) #
    # pdf = pisa.pisaDocument(BytesIO(html.encode("iso-8859-6")), result)
    # pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
        
    # print(type(html.encode('utf8')))#(var.encode('utf8'))
    # print((bytes(b,'utf-8')))
    # https://stackoverflow.com/questions/60139294/rendering-pdf-template-in-django-in-arabic-language
    # pdf = pisa.pisaDocument(BytesIO(html.encode('cp1252')), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


#################################

def get_last_month_data(today):
    '''
    Simple method to get the datetime objects for the 
    start and end of last month. 
    '''
    this_month_start = datetime.datetime(today.year, today.month, 1)
    last_month_end = this_month_start - datetime.timedelta(days=1)
    last_month_start = datetime.datetime(last_month_end.year, last_month_end.month, 1)
    return (last_month_start, last_month_end)


def get_month_data_range(months_ago=1, include_this_month=False):
    '''
    A method that generates a list of dictionaires 
    that describe any given amout of monthly data.
    '''
    today = datetime.datetime.now().today()
    dates_ = []
    if include_this_month:
        # get next month's data with:
        next_month = today.replace(day=28) + datetime.timedelta(days=4)
        # use next month's data to get this month's data breakdown
        start, end = get_last_month_data(next_month)
        dates_.insert(0, {
            "start": start.timestamp(),
            "end": end.timestamp(),
            "start_json": start.isoformat(),
            "end": end.timestamp(),
            "end_json": end.isoformat(),
            "timesince": 0,
            "year": start.year,
            "month": str(start.strftime("%B")),
            })
    for x in range(0, months_ago):
        start, end = get_last_month_data(today)
        today = start
        dates_.insert(0, {
            "start": start.timestamp(),
            "start_json": start.isoformat(),
            "end": end.timestamp(),
            "end_json": end.isoformat(),
            "timesince": int((datetime.datetime.now() - end).total_seconds()),
            "year": start.year,
            "month": str(start.strftime("%B"))
        })
    #dates_.reverse()
    return dates_ 


def get_filename(path): #/abc/filename.mp4
    return os.path.basename(path)


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_key_generator(instance):
    """
    This is for a Django project with an key field
    """
    size = random.randint(30, 45)
    key = random_string_generator(size=size)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(key=key).exists()
    if qs_exists:
        return unique_slug_generator(instance)
    return key


def unique_order_id_generator(instance):
    """
    This is for a Django project with an order_id field
    """
    order_new_id = random_string_generator()

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(order_id=order_new_id).exists()
    if qs_exists:
        return unique_slug_generator(instance)
    return order_new_id


def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance 
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug