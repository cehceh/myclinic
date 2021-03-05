# Generated by Django 2.2.13 on 2021-03-02 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gyno', '0003_auto_20210301_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='obestetric',
            name='obdate',
            field=models.DateField(blank=True, null=True, verbose_name='Follow Up Date:'),
        ),
        migrations.AlterField(
            model_name='drughistory',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Drug History:'),
        ),
        migrations.AlterField(
            model_name='gynhistory',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Gynecological History:'),
        ),
        migrations.AlterField(
            model_name='medhistory',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Medical History:'),
        ),
        migrations.AlterField(
            model_name='menstrual',
            name='edd',
            field=models.DateField(blank=True, null=True, verbose_name='EDD:'),
        ),
        migrations.AlterField(
            model_name='menstrual',
            name='ga',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='G.A:'),
        ),
        migrations.AlterField(
            model_name='menstrual',
            name='lmp',
            field=models.DateField(blank=True, null=True, verbose_name='LMP:'),
        ),
        migrations.AlterField(
            model_name='menstrual',
            name='remain',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Remaining:'),
        ),
        migrations.AlterField(
            model_name='obestetric',
            name='a',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='A:'),
        ),
        migrations.AlterField(
            model_name='obestetric',
            name='cs',
            field=models.BooleanField(default=False, verbose_name='CS:'),
        ),
        migrations.AlterField(
            model_name='obestetric',
            name='g',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='G:'),
        ),
        migrations.AlterField(
            model_name='obestetric',
            name='gyn',
            field=models.BooleanField(default=False, verbose_name='Gyn:'),
        ),
        migrations.AlterField(
            model_name='obestetric',
            name='hist',
            field=models.TextField(blank=True, max_length=250, null=True, verbose_name='History of previous obestetric complication(if any):'),
        ),
        migrations.AlterField(
            model_name='obestetric',
            name='lc',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='LC:'),
        ),
        migrations.AlterField(
            model_name='obestetric',
            name='ld',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='LD:'),
        ),
        migrations.AlterField(
            model_name='obestetric',
            name='nvd',
            field=models.BooleanField(default=False, verbose_name='NVD:'),
        ),
        migrations.AlterField(
            model_name='obestetric',
            name='p',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='P:'),
        ),
        migrations.AlterField(
            model_name='obestetric',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patientdata.Patients', verbose_name='Patient Name:'),
        ),
        migrations.AlterField(
            model_name='surhistory',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Surgical History:'),
        ),
    ]