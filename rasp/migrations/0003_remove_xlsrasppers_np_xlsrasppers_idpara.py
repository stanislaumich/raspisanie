# Generated by Django 4.2.13 on 2024-06-12 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('para', '0001_initial'),
        ('rasp', '0002_xlsrasppers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='xlsrasppers',
            name='np',
        ),
        migrations.AddField(
            model_name='xlsrasppers',
            name='idpara',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='para.para', verbose_name='Пара'),
        ),
    ]
