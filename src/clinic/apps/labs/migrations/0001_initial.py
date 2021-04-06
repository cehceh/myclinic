# Generated by Django 2.2.13 on 2021-04-03 15:03

import apps.labs.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('visits', '0001_initial'),
        ('patientdata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabVisit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Add analysis Here Please ....', max_length=100)),
                ('result', models.CharField(blank=True, max_length=150, null=True)),
                ('resdate', models.DateField(default=django.utils.timezone.now)),
                ('image', models.ImageField(blank=True, null=True, upload_to=apps.labs.models.upload_image_path)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patientdata.Patients')),
                ('visit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visits.Visits')),
            ],
        ),
        migrations.CreateModel(
            name='LabFollowup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Add analysis Here Please ....', max_length=100)),
                ('result', models.CharField(blank=True, max_length=150, null=True)),
                ('resdate', models.DateField(default=django.utils.timezone.now)),
                ('image', models.ImageField(blank=True, null=True, upload_to=apps.labs.models.upload_image_path)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('followup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visits.Visits')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patientdata.Patients')),
            ],
        ),
    ]