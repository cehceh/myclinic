@ECHO OFF

start cmd.exe /k "D: && activate clinicenv && echo activating.. && cd D:\Django\projects\myclinic\src\ && ^
python clinic\manage.py makemigrations --settings=clinic.settings.development && ^
echo makemigrations_db .. && ^
python clinic\manage.py migrate --settings=clinic.settings.development && ^
echo migrate_db .. && ^
python clinic\manage.py makemigrations accounts --settings=clinic.settings.development && ^
python clinic\manage.py migrate accounts --settings=clinic.settings.development && ^
python clinic\manage.py makemigrations patientdata --settings=clinic.settings.development && ^
python clinic\manage.py migrate patientdata --settings=clinic.settings.development && ^
python clinic\manage.py makemigrations visits --settings=clinic.settings.development && ^
python clinic\manage.py migrate visits --settings=clinic.settings.development && ^
python clinic\manage.py makemigrations visitdrug --settings=clinic.settings.development && ^
python clinic\manage.py migrate visitdrug --settings=clinic.settings.development && ^
python clinic\manage.py makemigrations revisits --settings=clinic.settings.development && ^
python clinic\manage.py migrate revisits --settings=clinic.settings.development && ^
python clinic\manage.py makemigrations revisitdrug --settings=clinic.settings.development && ^
python clinic\manage.py migrate revisitdrug --settings=clinic.settings.development && ^
python clinic\manage.py makemigrations pasthistory --settings=clinic.settings.development ^
python clinic\manage.py migrate pasthistory --settings=clinic.settings.development && ^
python clinic\manage.py makemigrations presenthistory --settings=clinic.settings.development && ^
python clinic\manage.py migrate presenthistory --settings=clinic.settings.development && ^
python clinic\manage.py makemigrations booking --settings=clinic.settings.development && ^
python clinic\manage.py migrate booking --settings=clinic.settings.development && ^
python clinic\manage.py makemigrations gyno --settings=clinic.settings.development && ^
python clinic\manage.py migrate gyno --settings=clinic.settings.development && ^
python clinic\manage.py makemigrations labs --settings=clinic.settings.development && ^
python clinic\manage.py migrate labs --settings=clinic.settings.development"
