# Generated by Django 2.2.13 on 2021-04-04 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientdata', '0004_auto_20210404_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='phone',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
