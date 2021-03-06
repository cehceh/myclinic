# Generated by Django 2.2.13 on 2021-04-05 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientdata', '0005_auto_20210404_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='patients',
            name='barcode',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='patients',
            name='barimg',
            field=models.ImageField(blank=True, null=True, upload_to='patient_barcode'),
        ),
    ]
