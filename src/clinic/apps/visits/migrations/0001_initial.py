# Generated by Django 2.2.13 on 2021-04-03 14:46

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patientdata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitdate', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('complain', models.TextField(blank=True, default='comp', null=True)),
                ('sign', models.TextField(blank=True, default='sign', null=True)),
                ('diagnosis', models.CharField(blank=True, max_length=150, null=True)),
                ('intervention', models.CharField(blank=True, max_length=150, null=True)),
                ('amount', models.IntegerField(default=0)),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patientdata.Patients')),
            ],
        ),
    ]
