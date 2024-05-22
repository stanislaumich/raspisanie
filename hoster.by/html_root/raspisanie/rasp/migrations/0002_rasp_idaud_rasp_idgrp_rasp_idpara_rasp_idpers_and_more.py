# Generated by Django 5.0.6 on 2024-05-17 13:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rasp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rasp',
            name='idaud',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='rasp.aud'),
        ),
        migrations.AddField(
            model_name='rasp',
            name='idgrp',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='rasp.grp'),
        ),
        migrations.AddField(
            model_name='rasp',
            name='idpara',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='rasp.para'),
        ),
        migrations.AddField(
            model_name='rasp',
            name='idpers',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='rasp.person'),
        ),
        migrations.AddField(
            model_name='rasp',
            name='idpredmet',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='rasp.predmet'),
        ),
        migrations.AlterField(
            model_name='para',
            name='num',
            field=models.IntegerField(default=0),
        ),
    ]
