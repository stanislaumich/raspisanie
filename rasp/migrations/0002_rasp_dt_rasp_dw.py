# Generated by Django 5.0.6 on 2024-05-16 20:01

import datetime
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rasp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rasp',
            name='dt',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rasp',
            name='dw',
            field=models.IntegerField(default=datetime.datetime(2024, 5, 16, 20, 1, 14, 957660, tzinfo=datetime.timezone.utc), verbose_name='День недели'),
            preserve_default=False,
        ),
    ]
