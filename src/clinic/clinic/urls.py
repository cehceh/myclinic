"""clinic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.home.views import frontpage, dashboard
from django.conf import settings
from django.conf.urls.static import static

from apps.gyno.api import api



urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Frontpage 
    path('', frontpage, name='frontpage'),

    # Dashboard 
    path('dashboard/', dashboard, name='dashboard'),

    path('booking/', include('apps.booking.urls', namespace='booking')),
    path('gyn/', include('apps.gyno.urls', namespace='gyno')),
    path('lab/', include('apps.labs.urls', namespace='labs')),
    
    path('patientdata/', include('apps.patientdata.urls', namespace='patientdata')),
    path('pasthistory/', include('apps.pasthistory.urls', namespace='pasthistory')),
    path('presenthistory/', include('apps.presenthistory.urls', namespace='presenthistory')),
    path('revisitdrug/', include('apps.revisitdrug.urls', namespace='revisitdrug')),
    path('revisits/', include('apps.revisits.urls', namespace='revisits')),
    
    path('reports/', include('apps.reports.urls', namespace='reports')),
    
    path('search/', include('apps.search.urls', namespace='search')),
    
    path('visits/', include('apps.visits.urls', namespace='visits')),
    path('visitdrug/', include('apps.visitdrug.urls', namespace='visitdrug')),
    # path('', include('', namespace='')),
    # path('', include('', namespace='')),
    # path('', include('', namespace='')),
    # path('', include('', namespace='')),
    # path('', include('', namespace='')),
    path('api/', api.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
