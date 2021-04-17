@ECHO OFF

# Open development environment so you must use --settings 
# open command, activate anaconda environment and run the project 
start cmd.exe /k "D: && activate clinicenv && cd D:\Django\projects\myclinic\src\clinic\ && python manage.py runserver 0.0.0.0:8000 --settings=clinic.settings.development"

# Due to Anaconda problem we use pyhthon venv environment
# start cmd.exe /k "D: && D:\Django\win_envs\clenv\Scripts\activate && cd D:\Django\projects\myclinic\src\clinic\ && python manage.py runserver 0.0.0.0:8000 --settings=clinic.settings.development"


# open Opera browser
start C:\Users\Root\AppData\Local\Programs\Opera\launcher.exe "http://localhost:8000" 

       