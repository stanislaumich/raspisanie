# Generated by Django 4.2.13 on 2024-06-06 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('para', '0002_alter_para_num'),
        ('person', '0002_person_isadmin'),
        ('rasp', '0002_alter_rasp_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateField(null=True, verbose_name='Дата')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Название')),
                ('idpara', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='para.para', verbose_name='Пара')),
                ('idpers', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='person.person', verbose_name='Преподаватель')),
            ],
            options={
                'verbose_name': 'Резерв',
                'verbose_name_plural': 'Резерв',
                'ordering': ['id'],
            },
        ),
    ]