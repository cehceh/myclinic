@ECHO OFF

# Open development environment so you must use --settings 
# open command, activate env and run the project 
start cmd.exe /k "D: && activate clinicenv && cd D:\Django\projects\myclinic\src\clinic\ && python manage.py runserver 0.0.0.0:8000 --settings=clinic.settings.development"


# open Opera browser
start C:\Users\Root\AppData\Local\Programs\Opera\launcher.exe "http://localhost:8000" 

       