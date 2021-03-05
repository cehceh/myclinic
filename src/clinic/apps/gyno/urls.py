from django.urls import path
from .views import add_gyno


app_name = 'gyno'
urlpatterns = [
    path('add/new/visit/', add_gyno, name='add_gyno'),
]


