from django.urls import path
from .views import add_gyno, edit_gyno


app_name = 'gyno'
urlpatterns = [

    path('add/new/visit/for/patient/<int:patient_id>/', add_gyno, name='add_gyno'),
    path('edit/followup/visit/<int:obs_id>/for/patient/<int:patient_id>/',
        edit_gyno, name='edit_gyno'),
]


