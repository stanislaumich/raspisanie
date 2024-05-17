# Generated by Django 4.2.13 on 2024-05-17 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rasp', '0002_rasp_idaud_rasp_idgrp_rasp_idpara_rasp_idpers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rasp',
            name='idaud',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='rasp.aud', verbose_name='Аудитория'),
        ),
        migrations.AlterField(
            model_name='rasp',
            name='idgrp',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='rasp.grp', verbose_name='Группа'),
        ),
        migrations.AlterField(
            model_name='rasp',
            name='idpara',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='rasp.para', verbose_name='Пара'),
        ),
        migrations.AlterField(
            model_name='rasp',
            name='idpers',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='rasp.person', verbose_name='Преподаватель'),
        ),
        migrations.AlterField(
            model_name='rasp',
            name='idpredmet',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='rasp.predmet', verbose_name='Предмет'),
        ),
    ]