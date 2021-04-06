from django.urls import path
from .views import (add_lab_followup, edit_lab_followup,
                    add_lab_visit, edit_lab_visit,
                    delete_lab_visit)


app_name = 'labs'
urlpatterns = [

    path('add/lab/for/patient/<int:patient_id>/followup/visit/<int:followup_id>/', 
        add_lab_followup, name='add_lab_followup'),
    path('edit/lab/<int:lab_id>/patient/<int:patient_id>/followup/visit/<int:followup_id>/',
        edit_lab_followup, name='edit_lab_followup'),
    
    # path('table/for/add/followup/visit/', 
    #     delete_lab_visit, name='delete_lab_visit'),
    
]
