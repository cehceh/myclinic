# Generated by Django 2.2.13 on 2021-02-21 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('revisitdrug', '0001_initial'),
        ('visits', '0001_initial'),
        ('revisits', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='remedicine',
            name='revisit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='revisits.Revisits'),
        ),
        migrations.AddField(
            model_name='remedicine',
            name='visit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='visits.Visits'),
        ),
    ]
