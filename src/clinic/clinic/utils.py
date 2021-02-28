from django.core.exceptions import PermissionDenied
from django.contrib import messages
import os, re, uuid 
# from simple_decorators.apps.models import Entry


#
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


