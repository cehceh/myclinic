from django.urls import path
from .views import add_gyno, edit_gyno, add_followup_table


app_name = 'gyno'
urlpatterns = [

    path('add/followup/visit/for/patient/<int:patient_id>/', 
        add_gyno, name='add_gyno'),
    path('edit/followup/visit/<int:obs_id>/for/patient/<int:patient_id>/',
        edit_gyno, name='edit_gyno'),
    path('table/for/add/followup/visit/', 
        add_followup_table, name='add_followup_table'),
    
]


