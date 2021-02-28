# from django.contrib import admin
# from django.conf import settings
# from django.conf.urls.static import static
from django.urls import path
from .views import (save_book, table_book, 
                    edit_book, delete_item,
                    date_table, current_date_table)


app_name = 'booking'
urlpatterns = [
    path('create/booking/date/', save_book, name='save_book'),
    path('edit/booking/date/<int:id>/', edit_book, name='edit_book'),
    path('table/', table_book, name='table_book'),
    path('current/date/table/', current_date_table, name='current_date_table'),
    
    path('date/<int:year>/<int:month>/<int:day>/', date_table, name='date_table'),
    path('delete/<int:id>/<int:year>/<int:month>/<int:day>/', delete_item, name='delete_item'),
    

]