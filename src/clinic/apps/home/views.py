from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from django.contrib import messages
from django.conf import settings
from django.utils import translation
from clinic.utils import auth_required

# Create your views here.

# @auth_required
def frontpage(request):
    ''' Home page before user sign in '''
    context = {}
    return render(request, 'home/frontpage.html', context)


# @auth_required
# # handel changes between languages in frontpage 
# def en_frontpage(request): 
#     ''' Handeling English Language '''
#     # from django.utils import translation
#     user_language = 'en' 
#     translation.activate(user_language)
#     response = render(request, 'home/frontpage.html')
#     response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
#     return response


# def ar_frontpage(request): 
#     ''' Handeling Arabic Language '''
#     user_language = 'ar' 
#     translation.activate(user_language)
#     response = render(request, 'home/frontpage.html')
#     response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
#     return response


# def de_frontpage(request): 
#     ''' Handeling German Language '''
#     user_language = 'de' 
#     translation.activate(user_language)
#     response = render(request, 'home/frontpage.html')
#     response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
#     return response

#################################
# @auth_required
def dashboard(request):
    ''' Dashboard page main page means English'''
    # from xml.dom import minidom
    # # parse an xml file by name
    # mydoc = minidom.parse('myfile.xml')
    # items = mydoc.getElementsByTagName('item')
    # # num1 = items[0].firstChild.data          # access data
    # # attr1 = items[0].attributes['num'].value # access atribute name value
    # num2 = items[1].childNodes[0].data       # access data
    # # attr2 = items[1].attributes['num'].value # access atribute name value
    
    context = {
        # 'num2':num2,
    }
    return render(request, 'home/dashboard.html', context)


# def ar_dashboard(request): 
#     ''' Handeling dashboard Arabic Language '''
#     # from django.utils import translation
#     user_language = 'ar' 
#     translation.activate(user_language)
#     response = render(request, 'home/dashboard.html')
#     response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
#     return response


# def de_dashboard(request): 
#     ''' Handeling dashboard German Language '''
#     # from django.utils import translation
#     user_language = 'de' 
#     translation.activate(user_language)
#     response = render(request, 'home/dashboard.html')
#     response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
#     return response

################### For changing URL for every language ################   
# def change_language(request):
#     response = HttpResponseRedirect('/')
#     if request.method == 'POST':
#         language = request.POST.get('language')
#         if language:
#             if language != settings.LANGUAGE_CODE and [lang for lang in settings.LANGUAGES if lang[0] == language]:
#                 redirect_path = f'/{language}/'
#             elif language == settings.LANGUAGE_CODE:
#                 redirect_path = '/'
#             else:
#                 return response
#             translation.activate(language)
#             response = HttpResponseRedirect(redirect_path)
#             response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
#     return response


